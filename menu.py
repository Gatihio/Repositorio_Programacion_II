from Funciones import *

while True:
    print("******************************************")
    print("*****     SOFTWARE DE ESTADISTICA    *****")
    print("*****         VERSIÓN INICIAL        *****")
    print("******************************************")

    lista_muestras = []
    lista_muestras = AGREGAR_ELEMENTOS_INPUT(lista_muestras)
    numero_muestra = len(lista_muestras)
    print("Muestra: ", lista_muestras)
    print("Cantidad de datos: ", numero_muestra)
    
    while True:
        respuesta = input("¿Qué medidas desea conocer? 1 = MEDIDAS DE POSICIÓN | 2 = MEDIDAS DE DISPERSIÓN  | 3 = FRECUENCIAS | 4 = DISTRIBUCIÓN BINOMIAL | 5 = DISTRIBUCIÓN POISSON | 6 = Finalizar. \n ==> ")
        if int(respuesta) == 1:
            print("Seleccionaste < Medidas de Posición >")
            MEDIDAS_POSICION(lista_muestras)
        elif int(respuesta) == 2:
            print("Seleccionaste < Medidas de Dispersión >")
            MEDIDAS_DISPERCION(lista_muestras)
        elif int(respuesta) == 3:
            print("Seleccionaste < Frecuencias >")
            TABLAS_FRECUENCIAS(lista_muestras)
        elif int(respuesta) == 4:
            print("Seleccionaste < Distribución Binomial >")
            CALCULAR_PROBABILIDAD_BINOMIAL()
        elif int(respuesta) == 5:
            print("Seleccionaste < Distribución Poisson >")
            CALCULAR_PROBABILIDAD_POISSON()
        elif int(respuesta) == 6:
            print("Finalizando...")
            break
        else:
            print("Comando no válido, intente de nuevo")

    continuacion = input("¿Desea volver a empezar? Y = sí, cualquier cosa = no : ")
    if continuacion.isalpha():
        if continuacion.upper() == "Y":
            print("Volvemos a empezar!")
        else:
            print("Fin del programa.")
            break
    else:
        print("Fin del programa.")
        break
