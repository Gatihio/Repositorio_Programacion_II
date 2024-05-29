#Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario.
#El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n. 
#El programa debe manejar números enteros grandes y mostrar el resultado.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    def main():
        try:
            numero = int(input("Ingrese un numero factorial: "))
            if numero <0:
               print("El factorial no esta designado para un numero negativo")
            else:
                print("El factorial de", numero, "es: ", factorial(numero))
        except ValorError:
            print ("La operacion no se puede realizar a menos que ingrese un numero valido")

if __name__ == "__main__":
    main()