#Producto de elementos: Escribe una función que tome una lista de números y
#devuelva el producto de todos los elementos.

def productos_elementos(lista):
    productos = 1
    for elementos in lista:
        productos *= elementos
        return productos
    
numeros = [10, 15, 20, 25, 30]
resultado = productos_elementos(numeros)
print("El producto de los elementos es:", resultado)