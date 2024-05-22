print("Para convertir de celcius a Fahrenheit presione 1")
print("Para convertir de Fahrenheit a celcius presione 2")
valor = int(input("Ingrese el valor: "))
if valor == 1:
    celcius = float(input("Ingrese en grados celcius"))
    resultado = (celcius * 9 / 5) + 32
    print("La convecion es de: ", resultado)
if valor == 2:
    Faherenheit = float(input("Ingrese en grados Fahrenheit"))
    resultado = (Faherenheit - 32) * 5 / 9
    print("La convecion es de: ", resultado)