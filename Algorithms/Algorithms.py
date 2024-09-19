import math


# Función para ingresar los procesos
def ingresar_procesos():
    n = int(input("Ingrese el número de procesos: "))  # RF1
    procesos = []

    for i in range(n):  # RF2
        nombre = input(f"Ingrese el nombre del proceso {i + 1}: ")
        ticks_cpu = int(input(f"Ingrese el número de ticks de CPU (Tiempo de ejecución) del proceso {nombre}: "))
        tiempo_llegada = int(input(f"Ingrese el tiempo de llegada del proceso {nombre}: "))
        prioridad = int(
            input(f"Ingrese la prioridad del proceso {nombre} (entre más bajo el número, mayor prioridad): "))

        procesos.append({
            'nombre': nombre,
            'ticks_cpu': ticks_cpu,
            'tiempo_llegada': tiempo_llegada,
            'prioridad': prioridad
        })

    return procesos


# Función para seleccionar algoritmo de planificación
def seleccionar_algoritmo():
    print("\nSeleccione el algoritmo de planificación de procesos:")
    print("1. FCFS")
    print("2. SJF")
    print("3. Prioridad")
    print("4. Round Robin")
    opcion = int(input("Ingrese el número de la opción: "))  # RF3
    return opcion


# FCFS - Primer llegado, primer servido
def fcfs(procesos):
    procesos_ordenados = sorted(procesos, key=lambda p: p['tiempo_llegada'])
    tiempo_actual = 0
    tiempos_espera = []
    tiempos_retorno = []

    print("\nSimulación de FCFS:")
    for proceso in procesos_ordenados:
        if tiempo_actual < proceso['tiempo_llegada']:
            tiempo_actual = proceso['tiempo_llegada']  # Considerar tiempos muertos

        ciclo_inicial = tiempo_actual
        ciclo_final = tiempo_actual + proceso['ticks_cpu']
        tiempo_actual = ciclo_final

        tiempos_espera.append(ciclo_inicial - proceso['tiempo_llegada'])
        tiempos_retorno.append(ciclo_final - proceso['tiempo_llegada'])

        print(f"Proceso {proceso['nombre']} - Ciclo inicial: {ciclo_inicial}, Ciclo final: {ciclo_final}")  # RF4

    return tiempos_espera, tiempos_retorno


# SJF - Shortest Job First
def sjf(procesos):
    procesos_ordenados = sorted(procesos, key=lambda p: (p['tiempo_llegada'], p['ticks_cpu']))
    tiempo_actual = 0
    tiempos_espera = []
    tiempos_retorno = []

    print("\nSimulación de SJF:")
    for proceso in procesos_ordenados:
        if tiempo_actual < proceso['tiempo_llegada']:
            tiempo_actual = proceso['tiempo_llegada']

        ciclo_inicial = tiempo_actual
        ciclo_final = tiempo_actual + proceso['ticks_cpu']
        tiempo_actual = ciclo_final

        tiempos_espera.append(ciclo_inicial - proceso['tiempo_llegada'])
        tiempos_retorno.append(ciclo_final - proceso['tiempo_llegada'])

        print(f"Proceso {proceso['nombre']} - Ciclo inicial: {ciclo_inicial}, Ciclo final: {ciclo_final}")

    return tiempos_espera, tiempos_retorno


# Prioridad - Basado en la prioridad del proceso
def prioridad(procesos):
    procesos_ordenados = sorted(procesos, key=lambda p: (p['tiempo_llegada'], p['prioridad']))
    tiempo_actual = 0
    tiempos_espera = []
    tiempos_retorno = []

    print("\nSimulación de Prioridad:")
    for proceso in procesos_ordenados:
        if tiempo_actual < proceso['tiempo_llegada']:
            tiempo_actual = proceso['tiempo_llegada']

        ciclo_inicial = tiempo_actual
        ciclo_final = tiempo_actual + proceso['ticks_cpu']
        tiempo_actual = ciclo_final

        tiempos_espera.append(ciclo_inicial - proceso['tiempo_llegada'])
        tiempos_retorno.append(ciclo_final - proceso['tiempo_llegada'])

        print(f"Proceso {proceso['nombre']} - Ciclo inicial: {ciclo_inicial}, Ciclo final: {ciclo_final}")

    return tiempos_espera, tiempos_retorno


# Round Robin
def round_robin(procesos):
    ticks_promedio = sum([p['ticks_cpu'] for p in procesos]) / len(procesos)
    quantum = math.ceil(0.8 * ticks_promedio)  # RF3: 80% del promedio de ticks de CPU
    tiempo_actual = 0
    cola = procesos.copy()
    tiempos_espera = {p['nombre']: 0 for p in procesos}
    tiempos_retorno = {p['nombre']: 0 for p in procesos}
    tiempos_finalizados = {p['nombre']: 0 for p in procesos}

    print("\nSimulación de Round Robin (Quantum = {}):".format(quantum))
    while cola:
        proceso = cola.pop(0)
        if tiempo_actual < proceso['tiempo_llegada']:
            tiempo_actual = proceso['tiempo_llegada']

        ciclo_inicial = tiempo_actual
        tiempo_restante = proceso['ticks_cpu'] - tiempos_finalizados[proceso['nombre']]
        ejecutar_ticks = min(quantum, tiempo_restante)
        ciclo_final = tiempo_actual + ejecutar_ticks
        tiempo_actual = ciclo_final
        tiempos_finalizados[proceso['nombre']] += ejecutar_ticks

        print(f"Proceso {proceso['nombre']} - Ciclo inicial: {ciclo_inicial}, Ciclo final: {ciclo_final}")

        if tiempos_finalizados[proceso['nombre']] < proceso['ticks_cpu']:
            cola.append(proceso)
        else:
            tiempos_retorno[proceso['nombre']] = ciclo_final - proceso['tiempo_llegada']
            tiempos_espera[proceso['nombre']] = tiempos_retorno[proceso['nombre']] - proceso['ticks_cpu']

    return list(tiempos_espera.values()), list(tiempos_retorno.values())


# Función para calcular los tiempos promedios
def calcular_promedios(tiempos_espera, tiempos_retorno):
    promedio_espera = sum(tiempos_espera) / len(tiempos_espera)
    promedio_retorno = sum(tiempos_retorno) / len(tiempos_retorno)
    print(f"\nTiempo promedio de espera: {promedio_espera:.2f}")  # RF5
    print(f"Tiempo promedio de retorno: {promedio_retorno:.2f}")  # RF6


# Función principal
def main():
    procesos = ingresar_procesos()
    algoritmo = seleccionar_algoritmo()

    if algoritmo == 1:
        tiempos_espera, tiempos_retorno = fcfs(procesos)
    elif algoritmo == 2:
        tiempos_espera, tiempos_retorno = sjf(procesos)
    elif algoritmo == 3:
        tiempos_espera, tiempos_retorno = prioridad(procesos)
    elif algoritmo == 4:
        tiempos_espera, tiempos_retorno = round_robin(procesos)
    else:
        print("Opción inválida")
        return

    calcular_promedios(tiempos_espera, tiempos_retorno)


# Ejecución del programa
if __name__ == "__main__":
    main()
