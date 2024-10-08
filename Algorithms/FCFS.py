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
