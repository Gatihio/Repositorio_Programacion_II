#10.Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
#índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.

def buscar_indice(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
        return -1
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valor = 5
indice = buscar_indice(numeros, valor)
if indice != -1:
    print("El valor", valor, "se encuentra en el índice:", indice)
else:
    print("El valor", valor, "no está presente en la lista.")