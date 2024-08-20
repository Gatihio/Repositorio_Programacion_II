import math
from collections import defaultdict

# FUNCIONES BÁSICAS

def AGREGAR_ELEMENTOS_INPUT():
    lista = []
    numero_muestra = 0
    print("Ingrese los datos uno por uno, y presione enter para continuar. Ingrese 'FIN' para finalizar.")
    while True:
        valor = input(f"Ingrese dato número {numero_muestra + 1}: ")
        if valor.isdigit():
            lista.append(float(valor))
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de la muestra")
                break
            else:
                print("Comando no válido, intente de nuevo.")
        else:
            try:
                valor = float(valor)
                lista.append(valor)
                numero_muestra += 1
            except:
                print("Comando no válido, intente de nuevo.")
    
    lista = sorted(lista)
    return lista

def MEDIA(lista):
    return sum(lista) / len(lista)

def MEDIANA(lista):
    n = len(lista)
    lista_ordenada = sorted(lista)
    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return mediana

def MODA(lista):
    frecuencias = defaultdict(int)
    for valor in lista:
        frecuencias[valor] += 1
    max_frecuencia = max(frecuencias.values())
    modas = [valor for valor, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
    return modas

def RANGO(lista):
    return max(lista) - min(lista)

def VARIANZA(lista):
    media = MEDIA(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)

def DESVIACION_ESTANDAR(lista):
    return math.sqrt(VARIANZA(lista))

def FRECUENCIAS(lista):
    frecuencias = defaultdict(int)
    for valor in lista:
        frecuencias[valor] += 1
    for valor, frecuencia in frecuencias.items():
        print(f"Valor: {valor}, Frecuencia: {frecuencia}")

# FUNCIONES DE PROBABILIDAD

def DISTRIBUCION_BINOMIAL(n, p, k):
    coef_binomial = math.comb(n, k)
    probabilidad = coef_binomial * (p ** k) * ((1 - p) ** (n - k))
    return probabilidad

def DISTRIBUCION_POISSON(lmbda, k):
    probabilidad = (math.exp(-lmbda) * (lmbda ** k)) / math.factorial(k)
    return probabilidad

def ESPACIO_FINITO_PROBABILIDADES(eventos, espacio_muestral):
    probabilidad = len(eventos) / len(espacio_muestral)
    return probabilidad

def PROBABILIDAD_CONDICIONAL(probabilidad_A, probabilidad_B_dado_A):
    return probabilidad_A * probabilidad_B_dado_A

def TEOREMA_DE_BAYES(probabilidad_A, probabilidad_B_dado_A, probabilidad_B):
    probabilidad_A_dado_B = (probabilidad_B_dado_A * probabilidad_A) / probabilidad_B
    return probabilidad_A_dado_B

def ESPERANZA_MATEMATICA(valores, probabilidades):
    esperanza = sum(val * prob for val, prob in zip(valores, probabilidades))
    return esperanza

def VARIANZA_PROBABILIDADES(valores, probabilidades, esperanza):
    varianza = sum((val - esperanza) ** 2 * prob for val, prob in zip(valores, probabilidades))
    return varianza

# MENU PRINCIPAL

def MENU():
    lista = []
    print("Bienvenido al módulo de Estadística Descriptiva y Probabilidad.")
    while True:
        opcion = int(input("1 = INGRESAR DATOS\n2 = MEDIDAS DE POSICIÓN\n3 = MEDIDAS DE DISPERSIÓN\n4 = FRECUENCIAS\n5 = DISTRIBUCIONES DISCRETAS Y CONTINUAS\n6 = PROBABILIDAD Y EVENTOS\n7 = ESPERANZA MATEMÁTICA Y VARIANZA\n8 = SALIR\n ==> "))
        if opcion == 1:
            lista = AGREGAR_ELEMENTOS_INPUT()
        elif opcion == 2:
            if lista:
                print(f"Media: {MEDIA(lista):.4f}")
                print(f"Mediana: {MEDIANA(lista):.4f}")
                modas = MODA(lista)
                print(f"Moda: {', '.join(map(str, modas))}")
            else:
                print("No hay datos disponibles. Ingrese los datos primero.")
        elif opcion == 3:
            if lista:
                print(f"Rango: {RANGO(lista):.4f}")
                print(f"Varianza: {VARIANZA(lista):.4f}")
                print(f"Desviación Estándar: {DESVIACION_ESTANDAR(lista):.4f}")
            else:
                print("No hay datos disponibles. Ingrese los datos primero.")
        elif opcion == 4:
            if lista:
                FRECUENCIAS(lista)
            else:
                print("No hay datos disponibles. Ingrese los datos primero.")
        elif opcion == 5:
            while True:
                comando = int(input("¿Qué desea calcular?\n 1 = DISTRIBUCIÓN BINOMIAL\n 2 = DISTRIBUCIÓN DE POISSON\n ==> "))
                if comando == 1:
                    n = int(input("Ingrese el número de ensayos (n): "))
                    p = float(input("Ingrese la probabilidad de éxito (p): "))
                    k = int(input("Ingrese el número de éxitos deseados (k): "))
                    resultado = DISTRIBUCION_BINOMIAL(n, p, k)
                    print(f"La probabilidad binomial de obtener {k} éxitos en {n} ensayos es: {resultado:.4f}")
                    break
                elif comando == 2:
                    lmbda = float(input("Ingrese el valor esperado de la distribución de Poisson (λ): "))
                    k = int(input("Ingrese el número de éxitos deseados (k): "))
                    resultado = DISTRIBUCION_POISSON(lmbda, k)
                    print(f"La probabilidad de Poisson de obtener {k} éxitos es: {resultado:.4f}")
                    break
                else:
                    print("Comando incorrecto, intente de nuevo.")
        elif opcion == 6:
            while True:
                comando = int(input("¿Qué desea calcular?\n 1 = ESPACIO FINITO DE PROBABILIDADES\n 2 = PROBABILIDAD CONDICIONAL\n 3 = TEOREMA DE BAYES\n ==> "))
                if comando == 1:
                    espacio_muestral = input("Ingrese el espacio muestral (separe los elementos con comas): ").split(",")
                    eventos = input("Ingrese los eventos de interés (separe los elementos con comas): ").split(",")
                    resultado = ESPACIO_FINITO_PROBABILIDADES(eventos, espacio_muestral)
                    print(f"La probabilidad de los eventos dados en un espacio finito es: {resultado:.4f}")
                    break
                elif comando == 2:
                    probabilidad_A = float(input("Ingrese la probabilidad de A (P(A)): "))
                    probabilidad_B_dado_A = float(input("Ingrese la probabilidad de B dado A (P(B|A)): "))
                    resultado = PROBABILIDAD_CONDICIONAL(probabilidad_A, probabilidad_B_dado_A)
                    print(f"La probabilidad condicional es: {resultado:.4f}")
                    break
                elif comando == 3:
                    probabilidad_A = float(input("Ingrese la probabilidad de A (P(A)): "))
                    probabilidad_B_dado_A = float(input("Ingrese la probabilidad de B dado A (P(B|A)): "))
                    probabilidad_B = float(input("Ingrese la probabilidad de B (P(B)): "))
                    resultado = TEOREMA_DE_BAYES(probabilidad_A, probabilidad_B_dado_A, probabilidad_B)
                    print(f"La probabilidad de A dado B usando el Teorema de Bayes es: {resultado:.4f}")
                    break
                else:
                    print("Comando incorrecto, intente de nuevo.")
        elif opcion == 7:
            valores = list(map(float, input("Ingrese los valores posibles de la variable aleatoria (separe los elementos con comas): ").split(",")))
            probabilidades = list(map(float, input("Ingrese las probabilidades asociadas a los valores (separe los elementos con comas): ").split(",")))

            esperanza = ESPERANZA_MATEMATICA(valores, probabilidades)
            varianza = VARIANZA_PROBABILIDADES(valores, probabilidades, esperanza)
            
            print(f"La esperanza matemática es: {esperanza:.4f}")
            print(f"La varianza es: {varianza:.4f}")
        elif opcion == 8:
            print("Gracias por utilizar el módulo. ¡Hasta luego!")
            break
        else:
            print("Comando incorrecto, intente de nuevo.")

if __name__ == "__main__":
    MENU()
    