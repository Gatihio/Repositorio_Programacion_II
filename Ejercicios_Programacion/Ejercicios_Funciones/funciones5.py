def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero para calcular su factorial: "))
            if numero < 0:
                print("El número debe ser mayor o igual a cero.")
            else:
                resultado = factorial(numero)
                print(f"El factorial de {numero} es: {resultado}")
                break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()