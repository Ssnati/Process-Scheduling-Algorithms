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
