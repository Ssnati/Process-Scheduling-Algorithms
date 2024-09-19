# Función para calcular los tiempos promedios
def calcular_promedios(tiempos_espera, tiempos_retorno):
    promedio_espera = sum(tiempos_espera) / len(tiempos_espera)
    promedio_retorno = sum(tiempos_retorno) / len(tiempos_retorno)
    print(f"\nTiempo promedio de espera: {promedio_espera:.2f}")  # RF5
    print(f"Tiempo promedio de retorno: {promedio_retorno:.2f}")  # RF6

