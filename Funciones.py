import math
from scipy.stats import binom, poisson

# MEDIDAS DE POSICIÓN

def MEDIA(lista):
    return sum(lista) / len(lista)
    
def CALCULAR_MODA(lista):
    Max_Contador = 0
    Modas = []
    
    for Numero in lista:
        Cont = 0
        for Elem in lista:
            if Elem == Numero:
                Cont += 1
        if Cont > Max_Contador:
            Max_Contador = Cont
            Modas = [Numero]
        elif Cont == Max_Contador and Numero not in Modas:
            Modas.append(Numero)

    if len(Modas) == len(set(lista)):  # set elimina duplicados
        return "No hay moda"
    else:
        return Modas
    
def CALCULAR_MEDIANA(lista):
    listaOrdenada = sorted(lista)
    longitudLista = len(listaOrdenada)
    
    if longitudLista % 2 == 0:
        medioIzq = listaOrdenada[longitudLista // 2 - 1]
        medioDer = listaOrdenada[longitudLista // 2]
        return (medioIzq + medioDer) / 2
    else:
        return listaOrdenada[longitudLista // 2]

def CALCULAR_PROMEDIO(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def CALCULAR_CUARTILES(lista):
    longitudLista = len(lista)
    mediana = CALCULAR_MEDIANA(lista)
    if longitudLista % 2 == 0:
        mitad_inferior = lista[:longitudLista // 2]
        mitad_superior = lista[longitudLista // 2:]
    else:
        mitad_inferior = lista[:longitudLista // 2]
        mitad_superior = lista[longitudLista // 2 + 1:]

    q1 = CALCULAR_MEDIANA(mitad_inferior)
    q2 = mediana
    q3 = CALCULAR_MEDIANA(mitad_superior)
    
    return q1, q2, q3

def DESVIACION_ESTANDAR(lista):
    n = len(lista)
    if n <= 1:
        return 0
    promedio = MEDIA(lista)
    suma_resta_cuadrado = sum((x - promedio) ** 2 for x in lista)
    desviacion = (suma_resta_cuadrado / (n - 1)) ** 0.5
    return round(desviacion, 4)

def RANGO(lista):
    return lista[-1] - lista[0]

# FRECUENCIAS

def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias

def CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista):
    frecuencias_absolutas = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    frecuencia_absoluta_acumulada = {}
    acumulador = 0
    for elemento, frecuencia in frecuencias_absolutas.items():
        acumulador += frecuencia
        frecuencia_absoluta_acumulada[elemento] = acumulador
    return frecuencia_absoluta_acumulada

def SOLO_UN_ELEMENTO(lista):
    return list(set(lista))

def CALCULAR_FRECUENCIA_RELATIVA(lista):
    frecuencia_relativa = []
    frecuencia_absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    lista_simple = SOLO_UN_ELEMENTO(lista)
    for elemento in lista_simple:
        absoluta = frecuencia_absoluta[elemento]
        frecuencia = absoluta / len(lista)
        frecuencia_relativa.append(round(frecuencia, 4))
    return frecuencia_relativa

def CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista):
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    frecuencia_relativa_acumulada = []
    total = 0
    for i in range(len(frecuencia_relativa)):
        total += frecuencia_relativa[i]
        frecuencia_relativa_acumulada.append(round(total, 4))
    return frecuencia_relativa_acumulada

def CALCULAR_FRECUENCIA_PORCENTUAL(lista):
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    return [elemento * 100 for elemento in frecuencia_relativa]

def CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista):
    frecuencia_porcentual = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
    frecuencia_porcentual_acumulada = []
    acumulada = 0
    for elemento in frecuencia_porcentual:
        acumulada += elemento
        frecuencia_porcentual_acumulada.append(round(acumulada, 2))
    return frecuencia_porcentual_acumulada

# INTERVALOS

def CALCULAR_AMPLITUD_INTERVALOS(datos):
    from math import sqrt
    minimo = min(datos)
    maximo = max(datos)
    numero_intervalos = sqrt(len(datos))
    amplitud = (maximo - minimo) / numero_intervalos
    return round(amplitud, 4)

def CALCULAR_INTERVALOS_CLASE(datos):
    from math import sqrt
    cantidad_datos = len(datos)
    numero_intervalos = sqrt(cantidad_datos)
    amplitud = CALCULAR_AMPLITUD_INTERVALOS(datos)
    
    limite_inferior = min(datos)
    limite_superior = limite_inferior + amplitud
    intervalos = []

    while limite_superior <= max(datos):
        intervalos.append((round(limite_inferior, 4), round(limite_superior, 4)))
        limite_inferior = limite_superior
        limite_superior += amplitud
    return intervalos

# COEFICIENTE DE CURTOSIS

def CALCULAR_CURTOSIS(lista):
    n = len(lista)
    if n < 4:
        return "Número insuficiente de datos para calcular la curtosis"
    
    media = MEDIA(lista)
    desviacion = DESVIACION_ESTANDAR(lista)
    suma_cuarta = sum((x - media) ** 4 for x in lista)
    
    kurtosis = (suma_cuarta / (n * (desviacion ** 4))) - 3
    return round(kurtosis, 4)

# DISTRIBUCIÓN BINOMIAL

def DISTRIBUCION_BINOMIAL(n, p, k, tipo):
    if tipo == 'exacto':
        return round(binom.pmf(k, n, p), 4)
    elif tipo == 'menor':
        return round(binom.cdf(k - 1, n, p), 4)
    elif tipo == 'menor_o_igual':
        return round(binom.cdf(k, n, p), 4)
    elif tipo == 'mayor':
        return round(1 - binom.cdf(k, n, p), 4)
    elif tipo == 'mayor_o_igual':
        return round(1 - binom.cdf(k - 1, n, p), 4)
    else:
        return "Tipo de cálculo no válido"

# DISTRIBUCIÓN POISSON

def DISTRIBUCION_POISSON(mu, k, tipo):
    if tipo == 'exacto':
        return round(poisson.pmf(k, mu), 4)
    elif tipo == 'menor':
        return round(poisson.cdf(k - 1, mu), 4)
    elif tipo == 'menor_o_igual':
        return round(poisson.cdf(k, mu), 4)
    elif tipo == 'mayor':
        return round(1 - poisson.cdf(k, mu), 4)
    elif tipo == 'mayor_o_igual':
        return round(1 - poisson.cdf(k - 1, mu), 4)
    else:
        return "Tipo de cálculo no válido"

# FUNCIONES DEL INPUT

def AGREGAR_ELEMENTOS_INPUT(lista):
    numero_muestra = 0
    print("Ingrese los datos uno por uno, y presione enter para confirmar y continuar agregando más datos. \nCuando ya no desee agregar más, coloque la palabra FIN")
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

def MEDIDAS_POSICION(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = MEDIA ARITMÉTICA.\n 2 = MODA.\n 3 = MEDIANA.\n 4 = MÁXIMO.\n 5 = MÍNIMO.\n 6 = CUARTILES.\n 7 = CURTOSIS.\n ==> "))
        if comando == 1:
            valor = "La > Media Aritmética < de la lista es "
            resultado = MEDIA(lista)
            break
        elif comando == 2:
            valor = "La > Moda < de la lista es "
            resultado = CALCULAR_MODA(lista)
            break
        elif comando == 3:
            valor = "La > Mediana < de la lista es "
            resultado = CALCULAR_MEDIANA(lista)
            break
        elif comando == 4:
            valor = "El > Máximo < de la lista es "
            resultado = lista[-1]
            break
        elif comando == 5:
            valor = "El > Mínimo < de la lista es "
            resultado = lista[0]
            break
        elif comando == 6:
            valor = "Los > Cuartiles < de la lista son "
            resultado = CALCULAR_CUARTILES(lista)
            break
        elif comando == 7:
            valor = "El > Coeficiente de Curtosis < de la lista es "
            resultado = CALCULAR_CURTOSIS(lista)
            break
        else:
            print("Comando incorrecto, intente de nuevo")
    
    print(lista)
    print(f"{valor}: ", resultado)

def MEDIDAS_DISPERCION(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = RANGO.\n 2 = DESVIACIÓN ESTÁNDAR.\n ==> "))
        if comando == 1:
            valor = "El > Rango < de la lista es "
            resultado = RANGO(lista)
            break
        elif comando == 2:
            valor = "La > Desviación Estándar < de la lista es "
            resultado = DESVIACION_ESTANDAR(lista)
            break
        else:
            print("Comando incorrecto, intente de nuevo")
    
    print(lista)
    print(f"{valor}: ", resultado)

def TABLAS_FRECUENCIAS(lista):
    print("Frecuencia Absoluta: ", CALCULAR_FRECUENCIA_ABSOLUTA(lista))
    print("Frecuencia Absoluta Acumulada: ", CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista))
    print("Frecuencia Relativa: ", CALCULAR_FRECUENCIA_RELATIVA(lista))
    print("Frecuencia Relativa Acumulada: ", CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista))
    print("Frecuencia Porcentual: ", CALCULAR_FRECUENCIA_PORCENTUAL(lista))
    print("Frecuencia Porcentual Acumulada: ", CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista))
    print("Intervalos de Clases: ", CALCULAR_INTERVALOS_CLASE(lista))

def CALCULAR_PROBABILIDAD_BINOMIAL():
    n = int(input("Ingrese el número de pruebas (n): "))
    p = float(input("Ingrese la probabilidad de éxito en cada prueba (p): "))
    k = int(input("Ingrese el número de éxitos deseados (k): "))
    tipo = input("Ingrese el tipo de cálculo (exacto, menor, menor_o_igual, mayor, mayor_o_igual): ")
    probabilidad = DISTRIBUCION_BINOMIAL(n, p, k, tipo)
    print(f"La probabilidad de obtener exactamente {k} éxitos en {n} pruebas es: {probabilidad}")

def CALCULAR_PROBABILIDAD_POISSON():
    mu = float(input("Ingrese la tasa de ocurrencias (λ): "))
    k = int(input("Ingrese el número de eventos (k): "))
    tipo = input("Ingrese el tipo de cálculo (exacto, menor, menor_o_igual, mayor, mayor_o_igual): ")
    probabilidad = DISTRIBUCION_POISSON(mu, k, tipo)
    print(f"La probabilidad de observar exactamente {k} eventos es: {probabilidad}")
