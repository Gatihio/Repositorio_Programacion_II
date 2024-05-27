#Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
#sin elementos duplicados.

def eliminar_repetidos(lista):
    sin_duplicados = list(set(lista))
    return sin_duplicados

numeros = [1, 2, 3, 4, 1, 2, 5, 6, 3]
resultado = eliminar_repetidos(numeros)
print("Lista sin duplicados:", resultado)