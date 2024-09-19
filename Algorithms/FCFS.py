# Función para calcular el tiempo de espera de cada proceso
def calcular_tiempo_espera(tiempos_llegada, tiempos_ejecucion):
    n = len(tiempos_llegada)
    tiempos_espera = [0] * n
    tiempos_completados = [0] * n

    # El primer proceso no espera
    tiempos_completados[0] = tiempos_llegada[0] + tiempos_ejecucion[0]

    for i in range(1, n):
        # El tiempo de completado del proceso anterior + el tiempo de ejecución del proceso actual
        tiempos_completados[i] = max(tiempos_completados[i - 1], tiempos_llegada[i]) + tiempos_ejecucion[i]
        tiempos_espera[i] = tiempos_completados[i] - tiempos_llegada[i] - tiempos_ejecucion[i]

    return tiempos_espera


# Función para calcular el tiempo de retorno de cada proceso
def calcular_tiempo_retorno(tiempos_llegada, tiempos_ejecucion):
    n = len(tiempos_llegada)
    tiempos_retorno = [0] * n
    tiempos_completados = [0] * n

    tiempos_completados[0] = tiempos_llegada[0] + tiempos_ejecucion[0]

    for i in range(1, n):
        tiempos_completados[i] = max(tiempos_completados[i - 1], tiempos_llegada[i]) + tiempos_ejecucion[i]
        tiempos_retorno[i] = tiempos_completados[i] - tiempos_llegada[i]

    return tiempos_retorno


# Función principal para FCFS
def fcfs(tiempos_llegada, tiempos_ejecucion):
    tiempos_espera = calcular_tiempo_espera(tiempos_llegada, tiempos_ejecucion)
    tiempos_retorno = calcular_tiempo_retorno(tiempos_llegada, tiempos_ejecucion)

    print("Proceso\tTiempo de Llegada\tTiempo de Ejecución\tTiempo de Espera\tTiempo de Retorno")
    for i in range(len(tiempos_llegada)):
        print(
            f"P{i + 1}\t\t{tiempos_llegada[i]}\t\t\t{tiempos_ejecucion[i]}\t\t\t{tiempos_espera[i]}\t\t\t{tiempos_retorno[i]}")

    promedio_espera = sum(tiempos_espera) / len(tiempos_espera)
    promedio_retorno = sum(tiempos_retorno) / len(tiempos_retorno)

    print(f"\nTiempo promedio de espera: {promedio_espera:.2f}")
    print(f"Tiempo promedio de retorno: {promedio_retorno:.2f}")


# Ejemplo de uso
tiempos_llegada = [0, 2, 4, 6]
tiempos_ejecucion = [3, 6, 4, 5]

fcfs(tiempos_llegada, tiempos_ejecucion)
