import statistics
from tabulate import tabulate

def calcular_media(lista):
    return round(statistics.mean(lista), 4)

def calcular_moda(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    
    moda_frecuencia_maxima = max(frecuencias.values())
    moda = [num for num, freq in frecuencias.items() if freq == moda_frecuencia_maxima]

    if len(set(frecuencias.values())) == 1:
        return None, None
    else:
        return moda, moda_frecuencia_maxima

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    return round(statistics.median(lista_ordenada), 4)

def calcular_desviacion(lista):
    desviacion_estandar = statistics.stdev(lista)
    return round(desviacion_estandar, 4)

def calcular_varianza(lista):
    varianza = statistics.variance(lista)
    return round(varianza, 4)

def frecuencia_absoluta(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    return frecuencias

def frecuencia_relativa(lista):
    total = len(lista)
    frec_abs = frecuencia_absoluta(lista)
    frec_relativa = {key: round(value / total, 4) for key, value in frec_abs.items()}
    return frec_relativa

def frecuencia_porcentual(lista):
    frec_rel = frecuencia_relativa(lista)
    frec_porcentual = {key: round(value * 100, 4) for key, value in frec_rel.items()}
    return frec_porcentual

def frecuencia_absoluta_acumulada(lista):
    frec_abs = frecuencia_absoluta(lista)
    acumulado = 0
    frec_abs_acum = {}
    for key, value in frec_abs.items():
        acumulado += value
        frec_abs_acum[key] = acumulado
    return frec_abs_acum

def frecuencia_relativa_acumulada(lista):
    total = len(lista)
    frec_rel = frecuencia_relativa(lista)
    acumulado = 0
    frec_rel_acum = {}
    for key, value in frec_rel.items():
        acumulado += value
        frec_rel_acum[key] = round(acumulado, 4)
    return frec_rel_acum

def frecuencia_porcentual_acumulada(lista):
    frec_porcent = frecuencia_porcentual(lista)
    acumulado = 0
    frec_porcent_acum = {}
    for key, value in frec_porcent.items():
        acumulado += value
        frec_porcent_acum[key] = round(acumulado, 4)
    return frec_porcent_acum

def menu():
    opcion = None
    try:
        print("\n")
        print("0. Para cerrar el menú.")
        print("1. Visualizar la MEDIA.")
        print("2. Visualizar la MODA.")
        print("3. Visualizar la MEDIANA.")
        print("4. Visualizar la DESVIACIÓN ESTÁNDAR.")
        print("5. Visualizar la VARIANZA.")
        print("6. Visualizar FRECUENCIA ABSOLUTA.")
        print("7. Visualizar FRECUENCIA RELATIVA.")
        print("8. Visualizar FRECUENCIA PORCENTUAL.")
        print("9. Visualizar FRECUENCIA ABSOLUTA ACUMULADA.")
        print("10. Visualizar FRECUENCIA RELATIVA ACUMULADA.")
        print("11. Visualizar FRECUENCIA PORCENTUAL ACUMULADA.\n")
        opcion = int(input("Ingrese el número de la opción que desea visualizar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
    return opcion

def ingresar_datos():
    cantidad = 0
    numeros = []
    print('Ingrese los datos uno por uno (ENTER), luego para ir al menú ingrese "n" \n')
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
            print(tabulate([["MEDIA", calcular_media(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 2:
            moda, frecuencia = calcular_moda(numeros)
            if moda is None:
                print("No hay moda en los datos.")
            else:
                print(tabulate([["MODA", f"{moda} (Frecuencia: {frecuencia})"]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 3:
            print(tabulate([["MEDIANA", calcular_mediana(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 4:
            print(tabulate([["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 5:
            print(tabulate([["VARIANZA", calcular_varianza(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 6:
            print(tabulate([["FRECUENCIA ABSOLUTA", frecuencia_absoluta(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 7:
            print(tabulate([["FRECUENCIA RELATIVA", frecuencia_relativa(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 8:
            print(tabulate([["FRECUENCIA PORCENTUAL", frecuencia_porcentual(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 9:
            print(tabulate([["FRECUENCIA ABSOLUTA ACUMULADA", frecuencia_absoluta_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 10:
            print(tabulate([["FRECUENCIA RELATIVA ACUMULADA", frecuencia_relativa_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 11:
            print(tabulate([["FRECUENCIA PORCENTUAL ACUMULADA", frecuencia_porcentual_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        else:
            print("Opción no válida.")
        
        opcion = menu()

if __name__ == "__main__":
    main()