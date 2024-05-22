import statistics

def calcular_media(lista):
    return statistics.mean(lista)

def calcular_moda(lista):
    return statistics.mode(lista)

def calcular_mediana(lista):
    return statistics.median(lista)

def calcular_desviacion(lista):
    desviacion_estandar = statistics.stdev(lista)
    return desviacion_estandar

def calcular_varianza(lista):
    varianza = statistics.variance(lista)
    return varianza

def menu():
    
    opcion = None
    
    try:
        
        print("\n")
        print("0. Para cerrar el menú.")
        print("1. Visualizar la MEDIA.")
        print("2. Visualizar la MODA.")
        print("3. Visualizar la MEDIANA.")
        print("4. Visualizar la DESVIACIÓN ESTÁNDAR.")
        print("5. Visualizar la VARIANZA.\n")
        
        opcion = int(input("Ingrese el número de la opción que desea visualizar: "))
    
    except ValueError:    
        print("Por favor, ingrese un número válido.")
    return opcion

def ingresar_datos():
    cantidad = 0
    numeros = []
    print('Cuando termine de ingresar los datos escriba "n" para abrir el menú \n')
    while True:
        numero = input(f"Ingrese el dato número {cantidad + 1}: ")
        if numero.lower() == "n":
            break
        else:
            try:
                numero = float(numero)
                cantidad += 1
                numeros.append(numero)
            except ValueError:
                print("Por favor, ingrese un número válido o escriba 'n' para terminar.")
    return numeros

def main():
    numeros = ingresar_datos()
    opcion = menu()
    
    while opcion != 0:
        
        if opcion == 1:
            print(f"La media es: {calcular_media(numeros)}")
        elif opcion == 2:
            print(f"La moda es: {calcular_moda(numeros)}")
        elif opcion == 3:
            print(f"La mediana es: {calcular_mediana(numeros)}")
        elif opcion == 4:
            print(f"La desviación es: {calcular_desviacion(numeros)}")
        elif opcion == 5:
            print(f"La varianza es: {calcular_varianza(numeros)}")
        else:
            print("Opción no válida.")
        
        opcion = menu()

if __name__ == "_main_":
    main()