def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:  
            suma += num   
    return suma

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = suma_pares(numeros)
print("La suma de los números pares en la lista es:", resultado)