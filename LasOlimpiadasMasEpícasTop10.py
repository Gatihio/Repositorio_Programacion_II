import matplotlib.pyplot as plt
import numpy as np

def plot_function(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.title('Gráfica de la función cuadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()

def gauss_jordan(matrix, vector):
    n = len(matrix)
    for i in range(n):
        # Buscamos el elemento pivote
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        vector[i], vector[max_row] = vector[max_row], vector[i]

        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("El sistema es incompatible o indeterminado.")

        for j in range(i, n):
            matrix[i][j] /= pivot
        vector[i] /= pivot

        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n):
                    matrix[k][j] -= factor * matrix[i][j]
                vector[k] -= factor * vector[i]

    return vector

def solve_system():
    matrix = []
    for i in range(3):
        row = [float(input(f"Ingrese el coeficiente a{i+1}{j+1}: ")) for j in range(3)]
        matrix.append(row)

    vector = [float(input(f"Ingrese el término independiente {i+1}: ")) for i in range(3)]

    solution = gauss_jordan(matrix, vector)

    print("Solución:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x:.2f}")

def calculate_area():
    a, b, c = map(float, input("Ingrese los coeficientes de la función cuadrática (a, b, c): ").split())
    interval = input("Ingrese el intervalo (a, b): ").split(',')
    a_interval, b_interval = float(interval[0]), float(interval[1])
    n = int(input("Ingrese la cantidad de rectángulos: "))

    def f(x):
        return a * x**2 + b * x + c

    x = np.linspace(a_interval, b_interval, n+1)
    y = f(x)

    dx = (b_interval - a_interval) / n
    lower_sum = sum(y[:-1]) * dx
    upper_sum = sum(y[1:]) * dx
    real_area = np.trapz(y, x)

    error = min(abs(real_area - lower_sum), abs(real_area - upper_sum))

    print("Suma inferior:", lower_sum)
    print("Suma superior:", upper_sum)
    print("Área real:", real_area)
    print("Error de cálculo:", error)

def main():
    while True:
        print("\n1. Resolver un sistema de ecuaciones")
        print("2. Calcular el área bajo la curva de una función cuadrática")
        print("3. Graficar la función cuadrática")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            solve_system()
        elif choice == '2':
            calculate_area()
        elif choice == '3':
            a, b, c = map(float, input("Ingrese los coeficientes de la función cuadrática (a, b, c): ").split())
            plot_function(a, b, c)
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "_main_":
    main()