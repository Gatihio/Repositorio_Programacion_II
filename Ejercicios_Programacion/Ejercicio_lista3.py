#Promedio de una lista: Crea una función que calcule el promedio de los números en
#una lista dada.

def calcular_promedio(lista):
    if not lista:
        return None
    
    suma_total = sum(lista)
    promedio = suma_total / len(lista)
    return promedio

numeros = [5, 3, 8, 1, 9, 2]
promedio = calcular_promedio(numeros)
print("El promedio de los números es:", promedio)