#Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
#cuántas veces aparece ese valor en la lista.

def contar_valor(lista, valor):
    contador = 0
    for elementos in lista:
        if elementos == valor:
            contador += 1
        return contador

numeros = [1, 2, 3, 4, 1, 2, 5, 6, 3]
valor = 2
apariciones = contar_valor(numeros, valor)
print("El valor", valor, "aparece", apariciones, "veces en la lista.")