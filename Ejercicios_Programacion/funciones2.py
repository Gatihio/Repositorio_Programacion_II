def calcularMaxMin(lista):
    if not lista:
        return None, None
    else:
        maximo = minimo = list[0]
        for num in lista:
            if num > maximo:
             maximo = num
             if num < minimo:
                minimo = num
        return maximo, minimo
    
def main():
    numeros = []
    while True:
        entrada = input("Introduce un número o 'listo' para terminar: ")
        if entrada.lower() == 'listo':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")

    maximo, minimo = calcularMaxMin(numeros)
    if maximo is not None and minimo is not None:
        print("El máximo es:", maximo)
        print("El mínimo es:", minimo)

if __name__ == "__main__":
    main()