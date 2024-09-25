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
    tiempos_finalizados = {p['nombre']: 0 for p in procesos}
    cola = []
    proceso_actual = None

    print("\nSimulación de SJF Expropiativo:")
    while procesos or cola or proceso_actual:
        # Añadir los procesos que han llegado a la cola
        while procesos and procesos[0]['tiempo_llegada'] <= tiempo_actual:
            proceso = procesos.pop(0)
            cola.append(proceso)

        # Elegir el proceso con el menor tiempo de ejecución restante
        if proceso_actual:
            cola.append(proceso_actual)

        if cola:
            # Elegir el proceso con menor ticks_cpu - tiempo_finalizado
            proceso_actual = min(cola, key=lambda p: (
                p['ticks_cpu'] - tiempos_finalizados[p['nombre']],
                1 if p == proceso_actual else 0  # Priorizar proceso actual si es igual
            ))
            cola.remove(proceso_actual)
        else:
            tiempo_actual += 1
            continue

        ciclo_inicial = tiempo_actual
        tiempo_restante = proceso_actual['ticks_cpu'] - tiempos_finalizados[proceso_actual['nombre']]
        siguiente_evento = procesos[0]['tiempo_llegada'] if procesos else float('inf')
        ejecutar_ticks = min(tiempo_restante, siguiente_evento - tiempo_actual)
        ciclo_final = tiempo_actual + ejecutar_ticks
        tiempo_actual = ciclo_final

        tiempos_finalizados[proceso_actual['nombre']] += ejecutar_ticks

        print(
            f"Proceso {proceso_actual['nombre']} - Ciclo inicial: {ciclo_inicial}, Ciclo final (parcial): {ciclo_final}")

        # Si el proceso ha terminado, calcular tiempo de retorno y esperar
        if tiempos_finalizados[proceso_actual['nombre']] == proceso_actual['ticks_cpu']:
            tiempos_retorno[proceso_actual['nombre']] = ciclo_final - proceso_actual['tiempo_llegada']
            tiempos_espera[proceso_actual['nombre']] = tiempos_retorno[proceso_actual['nombre']] - proceso_actual[
                'ticks_cpu']
            proceso_actual = None

    return list(tiempos_espera.values()), list(tiempos_retorno.values())
