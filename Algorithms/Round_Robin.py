import math
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
