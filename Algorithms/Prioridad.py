def prioridad(procesos):
    # Ordenamos los procesos por tiempo de llegada y prioridad
    procesos_ordenados = sorted(procesos, key=lambda p: (p['tiempo_llegada'], p['prioridad']))
    tiempo_actual = 0
    tiempos_espera = []
    tiempos_retorno = []
    completados = 0
    n = len(procesos)

    # Diccionario para almacenar el tiempo restante de cada proceso
    tiempo_restante = {p['nombre']: p['ticks_cpu'] for p in procesos_ordenados}

    print("\nSimulación de Prioridad Expropiativa:")

    # Mientras haya procesos por completar
    while completados < n:
        # Seleccionar el proceso con mayor prioridad que haya llegado y tenga tiempo restante
        proceso_actual = None
        for proceso in procesos_ordenados:
            if proceso['tiempo_llegada'] <= tiempo_actual and tiempo_restante[proceso['nombre']] > 0:
                if proceso_actual is None or proceso['prioridad'] < proceso_actual['prioridad']:
                    proceso_actual = proceso

        if proceso_actual is None:
            # Si no hay proceso que pueda ejecutarse, avanzamos el tiempo
            tiempo_actual += 1
            continue

        # Ejecución de un tick del proceso con mayor prioridad
        print(f"Proceso {proceso_actual['nombre']} ejecutando en el ciclo {tiempo_actual}")
        tiempo_restante[proceso_actual['nombre']] -= 1
        tiempo_actual += 1

        # Si el proceso ha terminado su ejecución
        if tiempo_restante[proceso_actual['nombre']] == 0:
            completados += 1
            ciclo_final = tiempo_actual
            ciclo_inicial = ciclo_final - proceso_actual['ticks_cpu']

            # Calcular tiempos de espera y retorno
            tiempos_espera.append(ciclo_inicial - proceso_actual['tiempo_llegada'])
            tiempos_retorno.append(ciclo_final - proceso_actual['tiempo_llegada'])

            print(f"Proceso {proceso_actual['nombre']} - Ciclo inicial: {ciclo_inicial}, Ciclo final: {ciclo_final}")

    return tiempos_espera, tiempos_retorno
