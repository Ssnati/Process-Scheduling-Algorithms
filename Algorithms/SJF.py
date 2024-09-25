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
    tiempos_espera = {p['nombre']: 0 for p in procesos}
    tiempos_retorno = {p['nombre']: 0 for p in procesos}

    # Ordenar los procesos por tiempo de llegada
    procesos.sort(key=lambda x: x['tiempo_llegada'])

    print("\nSimulación de SJF Expropiativo:")
    while procesos:
        # Filtrar procesos que han llegado
        lista_disponible = [p for p in procesos if p['tiempo_llegada'] <= tiempo_actual]

        if not lista_disponible:
            # Avanzar el tiempo si no hay procesos disponibles
            tiempo_actual = procesos[0]['tiempo_llegada']
            continue

        # Escoger el proceso con el menor tiempo de ejecución restante
        proceso_actual = min(lista_disponible, key=lambda x: x['ticks_cpu'])

        # Ejecutar el proceso actual durante 1 ciclo
        proceso_actual['ticks_cpu'] -= 1
        tiempo_actual += 1

        # Calcular tiempos de retorno y espera si el proceso ha terminado
        if proceso_actual['ticks_cpu'] == 0:
            ciclo_final = tiempo_actual
            tiempos_retorno[proceso_actual['nombre']] = ciclo_final - proceso_actual['tiempo_llegada']
            tiempos_espera[proceso_actual['nombre']] = tiempos_retorno[proceso_actual['nombre']] - procesos[procesos.index(proceso_actual)]['ticks_cpu']
            print(f"Proceso {proceso_actual['nombre']} terminado - Ciclo final: {ciclo_final}")
            procesos.remove(proceso_actual)

        # Actualizar tiempos de espera de los demás procesos
        for p in procesos:
            if p != proceso_actual and p['tiempo_llegada'] <= tiempo_actual:
                tiempos_espera[p['nombre']] += 1

    return list(tiempos_espera.values()), list(tiempos_retorno.values())
