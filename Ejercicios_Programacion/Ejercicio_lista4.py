#Elementos mayores que un valor: Escribe una función que tome una lista de números
#y un valor n, y devuelva una nueva lista con los elementos mayores que n.

def mayor_n(lista, n):
    elementos_mayores = [elemento for elemento in lista if elemento > n]
    return elementos_mayores

numeros = [5, 3, 8, 1, 9, 2]
valor_n = 4
resultados = mayor_n(numeros, valor_n)
print("Elementos mayores que", valor_n, ":", resultados)