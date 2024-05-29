import math

def area_radio(radio):
    return math.pi * radio ** 2

def perimertro_radio(radio):
    return 2 * math.pi * radio

def main(): 
    try:
        radio = float(input("Ingrese el radio de la sircunferencia: "))
        if radio <= 0:
            print("El radio debe estar en numeros positivos")
        else:
            area = area_radio(radio)
            perimetro = perimertro_radio(radio)
            print("El área de la circunferencia es:", area)
            print("El perímetro de la circunferencia es:", perimetro)
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número válido para el radio.")

if __name__ == "__main__":
    main()