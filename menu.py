from Funciones import *
import math

while True:
    print("******************************************")
    print("*****     SOFTWARE DE ESTADISTICA    *****")
    print("*****         VERSIÓN INICIAL        *****")
    print("******************************************")

    # Estas lineas son las que permiten que el usuario ingrese los datos, los cuales se almacenan en una lista, la cual se ordena de menor a mayor, y solo permite valores numéricos.
    lista_muestras = []
    lista_muestras = AGREGAR_ELEMENTOS_INPUT(lista_muestras)
    numero_muestra = len(lista_muestras)
    #En pantalla se imprime la lista de los elementos dados por el usuario y la cantidad de elementos que se ingresaron
    print("Muestra: ", lista_muestras)
    print("Cantidad de datos: ", numero_muestra)
    
    # Este es el main del código, aca se ejecuta todo el programa y se hacen las llamadas al documento "Funciones", del cual extraemos las funciones necesarias   
    while True: #Este while le permite al usuario utilizar tantas veces quiera las opciones que se ofrecen
        #La variable respuesta le permite al usuario escribir el valor de que tipo de informacion desea recibir de la lista de muestras
        respuesta = input("¿Que medidas desea conocer? 1 = MEDIDAS DE POSICIÓN | 2 = MEDIDAS DE DISPERCIÓN  | 3 = FRECUENCIAS | 4 = Finalizar. \n ==> ")
        if int(respuesta) == 1:
            print("Seleccionaste < Medidas de Posición >")
            resultado = MEDIDAS_POSICION(lista_muestras)
        elif int(respuesta) == 2:
            print("Seleccionaste < Medidas de Disperción >")
            resultado = MEDIDAS_DISPERCION(lista_muestras)
        elif int(respuesta) == 3:
            print("Seleccionaste < Frecuencias >")
            resultado = TABLAS_FRECUENCIAS(lista_muestras)
        elif int(respuesta) == 4:
            print("Finalizando...")
            break
        else:
            print("Comando no válido, intente de nuevo")
            
    #Falta aclarar algunos aspectos de esta parte del código
    #Aca se evalua si se quiere seguir utilizando el programa o no. En caso de que si, se escribe la Y, en caso de que no, se ingresa cualquier valor.
    continuacion = input("¿Desea volver a empezar? Y = si, cualquier cosa = no : ")
    if continuacion.isalpha():
        if continuacion.upper() == "Y":
            print("Volvemos a empezar!")
        else:
            print("Fin del programa.")
            break
    else:
        print("Fin del programa.")
        break

def menu_distribuciones():
    while True:
        try:
            print("\nDistribuciones - Seleccione una opción:")
            print("1. Distribución Binomial.")
            print("2. Distribución de Poisson.")
            print("3. Distribución Hipergeométrica.")
            print("4. Distribución Normal (Gaussiana).")
            print("0. Regresar al menú principal\n")

            opcion = int(input("Ingrese el número de la opción que desea utilizar: "))
            if opcion == 0:
                return
            elif opcion == 1:
                n = int(input("Ingrese el número de ensayos (n): "))
                p = float(input("Ingrese la probabilidad de éxito (p): "))
                k = int(input("Ingrese el número de éxitos deseados (k): "))
                resultado = distribucion_binomial(n, p, k)
                print(tabulate([["PROBABILIDAD BINOMIAL", resultado]], headers=["Operación", "Resultado"], tablefmt="grid"))
            elif opcion == 2:
                lambd = float(input("Ingrese el valor de lambda (λ): "))
                k = int(input("Ingrese el número de ocurrencias deseadas (k): "))
                resultado = distribucion_poisson(lambd, k)
                print(tabulate([["PROBABILIDAD DE POISSON", resultado]], headers=["Operación", "Resultado"], tablefmt="grid"))
            elif opcion == 3:
                n = int(input("Ingrese el tamaño de la muestra (n): "))
                M = int(input("Ingrese el número de éxitos en la población (M): "))
                N = int(input("Ingrese el tamaño de la población (N): "))
                k = int(input("Ingrese el número de éxitos deseados en la muestra (k): "))
                resultado = distribucion_hipergeometrica(n, M, N, k)
                print(tabulate([["PROBABILIDAD HIPERGEOMÉTRICA", resultado]], headers=["Operación", "Resultado"], tablefmt="grid"))
            elif opcion == 4:
                x = float(input("Ingrese el valor de x: "))
                mu = float(input("Ingrese la media (μ): "))
                sigma = float(input("Ingrese la desviación estándar (σ): "))
                resultado = distribucion_normal(x, mu, sigma)
                print(tabulate([["DISTRIBUCIÓN NORMAL", resultado]], headers=["Operación", "Resultado"], tablefmt="grid"))
            else:
                print("Opción no válida. Intente nuevamente o ingrese 0 para regresar al menú principal.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")