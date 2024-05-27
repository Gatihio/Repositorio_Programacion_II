#Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
#valor máximo y el mínimo de la lista.

def calcularMaxMin(lista):
    if not lista:
        return None, None
    else:
        maximo = minimo = list[0]
        for num in lista:
            if num > maximo:
             maximo = num
            elif num < minimo:
                minimo = num
            return maximo, minimo
    
numeros = [5, 3, 8, 1, 9, 2]
maximo, minimo = calcularMaxMin(numeros)
print("El máximo es:", maximo)
print("El mínimo es:", minimo)