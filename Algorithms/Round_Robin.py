import math


# Round Robin
def round_robin(procesos):
    ticks_promedio = sum([p['ticks_cpu'] for p in procesos]) / len(procesos)
    quantum = math.ceil(0.8 * ticks_promedio)  # 80% del promedio de ticks de CPU
    tiempo_actual = 0
    cola = []
    tiempos_espera = {p['nombre']: 0 for p in procesos}
    tiempos_retorno = {p['nombre']: 0 for p in procesos}
    tiempos_finalizados = {p['nombre']: 0 for p in procesos}
    procesos.sort(key=lambda p: p['tiempo_llegada'])  # Ordenar por tiempo de llegada

    print("\nSimulación de Round Robin (Quantum = {}):".format(quantum))

    while procesos or cola:
        # Agregar nuevos procesos a la cola
        while procesos and procesos[0]['tiempo_llegada'] <= tiempo_actual:
            cola.append(procesos.pop(0))

        if not cola:  # Si la cola está vacía, avanza el tiempo
            tiempo_actual = procesos[0]['tiempo_llegada'] if procesos else tiempo_actual
            continue

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

        # Agregar nuevos procesos en el momento que el proceso actual termina su quantum
        while procesos and procesos[0]['tiempo_llegada'] <= tiempo_actual:
            cola.append(procesos.pop(0))

        if tiempos_finalizados[proceso['nombre']] < proceso['ticks_cpu']:
            cola.append(proceso)  # Volver a agregar el proceso a la cola
        else:
            tiempos_retorno[proceso['nombre']] = ciclo_final - proceso['tiempo_llegada']
            tiempos_espera[proceso['nombre']] = tiempos_retorno[proceso['nombre']] - proceso['ticks_cpu']

    return list(tiempos_espera.values()), list(tiempos_retorno.values())
