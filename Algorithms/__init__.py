from Prioridad import prioridad
from FCFS import fcfs
from SJF import sjf_no_expropiativo, sjf_expropiativo
from Round_Robin import round_robin
from Tiempos_Promedios import calcular_promedios


# Función para ingresar los procesos
def ingresar_procesos():
    n = int(input("Ingrese el número de procesos: "))  # RF1
    procesos = []

    for i in range(n):  # RF2
        nombre = input(f"Ingrese el nombre del proceso {i + 1}: ")
        ticks_cpu = int(input(f"Ingrese el número de ticks de CPU (Tiempo de ejecución) del proceso {nombre}: "))
        tiempo_llegada = int(input(f"Ingrese el tiempo de llegada del proceso {nombre}: "))
        prioridad = int(
            input(f"Ingrese la prioridad del proceso {nombre} (entre más bajo el número, mayor prioridad): "))

        procesos.append({
            'nombre': nombre,
            'ticks_cpu': ticks_cpu,
            'tiempo_llegada': tiempo_llegada,
            'prioridad': prioridad
        })

    return procesos


# Función para seleccionar algoritmo de planificación
def seleccionar_algoritmo():
    print("\nSeleccione el algoritmo de planificación de procesos:")
    print("1. FCFS")
    print("2. SJF No expropiativo")
    print("3. SJF Expropiativo")
    print("4. Prioridad")
    print("5. Round Robin")
    print("0. Salir")
    opcion = int(input("Ingrese el número de la opción: "))  # RF3
    return opcion


# Función principal
def main():
    procesos = ingresar_procesos()
    algoritmo = seleccionar_algoritmo()
    while algoritmo != 0:
        if algoritmo == 1:
            tiempos_espera, tiempos_retorno = fcfs(procesos)
        elif algoritmo == 2:
            tiempos_espera, tiempos_retorno = sjf_no_expropiativo(procesos)
        elif algoritmo == 3:
            tiempos_espera, tiempos_retorno = sjf_expropiativo(procesos)
        elif algoritmo == 4:
            tiempos_espera, tiempos_retorno = prioridad(procesos)
        elif algoritmo == 5:
            tiempos_espera, tiempos_retorno = round_robin(procesos)
        else:
            print("Opción inválida")
            return
        calcular_promedios(tiempos_espera, tiempos_retorno)

        algoritmo = seleccionar_algoritmo()


# Ejecución del programa
if __name__ == "__main__":
    main()
