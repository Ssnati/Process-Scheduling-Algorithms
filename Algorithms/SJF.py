import math


# Shortest Job First (SJF) no expropiativo
def sjf_no_expropiativo(procesos):
    tiempo_actual = 0
    tiempos_espera = {p['nombre']: 0 for p in procesos}
    tiempos_retorno = {p['nombre']: 0 for p in procesos}

    # Ordenar los procesos por tiempo de llegada
    procesos.sort(key=lambda x: x['tiempo_llegada'])

    print("\nSimulación de SJF No Expropiativo:")
    while procesos:
        # Filtrar los procesos que han llegado
        lista_disponible = [p for p in procesos if p['tiempo_llegada'] <= tiempo_actual]

        if not lista_disponible:
            # Si no hay procesos disponibles, avanzar el tiempo
            tiempo_actual = procesos[0]['tiempo_llegada']
            continue

        # Escoger el proceso con el menor tiempo de ejecución
        proceso_actual = min(lista_disponible, key=lambda x: x['ticks_cpu'])

        # Calcular tiempos
        ciclo_inicial = tiempo_actual
        tiempo_actual += proceso_actual['ticks_cpu']
        ciclo_final = tiempo_actual

        # Guardar tiempos de retorno y espera
        tiempos_retorno[proceso_actual['nombre']] = ciclo_final - proceso_actual['tiempo_llegada']
        tiempos_espera[proceso_actual['nombre']] = tiempos_retorno[proceso_actual['nombre']] - proceso_actual[
            'ticks_cpu']

        # Imprimir el proceso y sus ciclos
        print(f"Proceso {proceso_actual['nombre']} - Ciclo inicial: {ciclo_inicial}, Ciclo final: {ciclo_final}")

        # Eliminar el proceso de la lista
        procesos.remove(proceso_actual)

    return list(tiempos_espera.values()), list(tiempos_retorno.values())


def sjf_expropiativo(procesos):
    tiempo_actual = 0
    completados = 0
    n = len(procesos)
    
    # Diccionario para almacenar el tiempo restante de cada proceso
    tiempo_restante = {p['nombre']: p['ticks_cpu'] for p in procesos}
    
    # Diccionario para almacenar el primer ciclo en que cada proceso empezó a ejecutarse
    tiempo_inicial = {p['nombre']: None for p in procesos}

    # Diccionarios para almacenar los tiempos de espera y retorno
    tiempos_espera = {p['nombre']: 0 for p in procesos}
    tiempos_retorno = {p['nombre']: 0 for p in procesos}

    # Ordenar los procesos por tiempo de llegada
    procesos_ordenados = sorted(procesos, key=lambda x: x['tiempo_llegada'])

    print("\nSimulación de SJF Expropiativo:")
    
    while completados < n:
        # Filtrar procesos que han llegado
        lista_disponible = [p for p in procesos_ordenados if p['tiempo_llegada'] <= tiempo_actual and tiempo_restante[p['nombre']] > 0]

        if not lista_disponible:
            # Avanzar el tiempo si no hay procesos disponibles
            tiempo_actual += 1
            continue

        # Escoger el proceso con el menor tiempo de ejecución restante
        proceso_actual = min(lista_disponible, key=lambda x: tiempo_restante[x['nombre']])

        # Registrar el ciclo inicial si es la primera vez que el proceso se ejecuta
        if tiempo_inicial[proceso_actual['nombre']] is None:
            tiempo_inicial[proceso_actual['nombre']] = tiempo_actual

        # Ejecutar el proceso actual durante 1 ciclo
        tiempo_restante[proceso_actual['nombre']] -= 1
        tiempo_actual += 1

        # Calcular tiempos de retorno y espera si el proceso ha terminado
        if tiempo_restante[proceso_actual['nombre']] == 0:
            completados += 1
            ciclo_final = tiempo_actual
            ciclo_inicial = tiempo_inicial[proceso_actual['nombre']]

            # Guardar tiempos de retorno y espera
            tiempos_retorno[proceso_actual['nombre']] = ciclo_final - proceso_actual['tiempo_llegada']
            tiempos_espera[proceso_actual['nombre']] = tiempos_retorno[proceso_actual['nombre']] - proceso_actual['ticks_cpu']

            print(f"Proceso {proceso_actual['nombre']} - Ciclo inicial: {ciclo_inicial}, Ciclo final: {ciclo_final}")

        # Actualizar tiempos de espera de los demás procesos
        for p in lista_disponible:
            if p != proceso_actual:
                tiempos_espera[p['nombre']] += 1

    return list(tiempos_espera.values()), list(tiempos_retorno.values())
