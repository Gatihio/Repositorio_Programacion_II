#Suma de elementos: Escribe una función que tome una lista de números y devuelva la
#suma de todos los elementos en la lista.

def suma_lista(lista):
    suma = 0
    for lista in lista:
        suma += lista
        return suma
    
def main():
    numeros = input("Ingresa los numeros separados: ").split()
    numeros = [int (num) for num in numeros]
    resultado = suma_lista(numeros)
    print("La suma de los elementos es: ", resultado)

    if __name__ == "__main__":
     main()