import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion(a, b, c, x1, x2, n):
    """Genera y muestra la gráfica de una función cuadrática y el área bajo la curva usando rectángulos."""
    x = np.linspace(x1, x2, 400)
    y = a * x**2 + b * x + c

    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')

    # Calcular el área usando el método de rectángulos
    dx = (x2 - x1) / n
    for i in range(n):
        x_rect = x1 + i * dx
        plt.bar(x_rect, a * x_rect**2 + b * x_rect + c, width=dx, align='edge', alpha=0.3, color='orange')

    plt.title('Gráfica de la función cuadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()

def obtener_coeficientes(entry_a, entry_b, entry_c):
    """Obtiene los coeficientes de la función cuadrática de las entradas."""
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        return a, b, c
    except ValueError:
        return None

def calcular_area_rectangulos(entry_a, entry_b, entry_c, entry_x1, entry_x2, entry_n):
    """Calcula el área bajo la curva usando el método de rectángulos."""
    a, b, c = obtener_coeficientes(entry_a, entry_b, entry_c)
    if a is None:
        return "Coeficientes inválidos"

    try:
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        n = int(entry_n.get())
    except ValueError:
        return "Entradas inválidas"

    def f(x):
        return a * x**2 + b * x + c

    dx = (x2 - x1) / n
    suma_inferior = sum(f(x1 + i * dx) * dx for i in range(n))
    suma_superior = sum(f(x1 + (i + 1) * dx) * dx for i in range(n))

    x_values = np.linspace(x1, x2, 1000)
    y_values = f(x_values)
    area_real = np.trapz(y_values, x_values)

    error_inferior = abs(area_real - suma_inferior)
    error_superior = abs(area_real - suma_superior)

    resultado = (f"Suma inferior: {suma_inferior:.4f}\n"
                 f"Suma superior: {suma_superior:.4f}\n"
                 f"Área real: {area_real:.4f}\n"
                 f"Error Suma Inferior: {error_inferior:.4f}\n"
                 f"Error Suma Superior: {error_superior:.4f}")

    return resultado

def resolver_sistema(matriz_entries, vector_entries, resultado_var):
    """Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Jordan."""
    matriz = []
    for entries in matriz_entries:
        try:
            fila = [float(entry.get()) for entry in entries]
            matriz.append(fila)
        except ValueError:
            resultado_var.set("Entradas inválidas")
            return

    vector = []
    for entry in vector_entries:
        try:
            vector.append(float(entry.get()))
        except ValueError:
            resultado_var.set("Entradas inválidas")
            return

    matriz_np = np.array(matriz)
    vector_np = np.array(vector)
    determinante = np.linalg.det(matriz_np)

    if determinante != 0:
        solucion = gauss_jordan(matriz, vector)
        resultado = "Solución:\n" + "\n".join([f"x{i+1} = {x:.2f}" for i, x in enumerate(solucion)])
        resultado_var.set(resultado)
    else:
        resultado_var.set("Sistema Incompatible o Indeterminado")

def gauss_jordan(matriz, vector):
    """Aplica el método de Gauss-Jordan para resolver el sistema."""
    n = len(matriz)
    for i in range(n):
        max_fila = max(range(i, n), key=lambda r: abs(matriz[r][i]))
        matriz[i], matriz[max_fila] = matriz[max_fila], matriz[i]
        vector[i], vector[max_fila] = vector[max_fila], vector[i]

        pivote = matriz[i][i]
        if pivote == 0:
            raise ValueError("El sistema es incompatible o indeterminado.")

        for j in range(i, n):
            matriz[i][j] /= pivote
        vector[i] /= pivote

        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(i, n):
                    matriz[k][j] -= factor * matriz[i][j]
                vector[k] -= factor * vector[i]

    return vector

def abrir_graficar_funcion():
    ventana_graficar = tk.Toplevel(root)
    ventana_graficar.title("Graficar Función Cuadrática")
    ventana_graficar.geometry("400x400")
    ventana_graficar.resizable(False, False)
    ventana_graficar.configure(bg="#f0f0f0")

    tk.Label(ventana_graficar, text="Coeficientes a, b, c:", bg="#f0f0f0").pack(pady=10)

    entry_a = tk.Entry(ventana_graficar, width=10)
    entry_a.pack(pady=5)
    entry_b = tk.Entry(ventana_graficar, width=10)
    entry_b.pack(pady=5)
    entry_c = tk.Entry(ventana_graficar, width=10)
    entry_c.pack(pady=5)

    tk.Label(ventana_graficar, text="Rango de visualización (x1, x2):", bg="#f0f0f0").pack(pady=10)
    entry_x1 = tk.Entry(ventana_graficar, width=10)
    entry_x1.pack(pady=5)
    entry_x2 = tk.Entry(ventana_graficar, width=10)
    entry_x2.pack(pady=5)

    tk.Label(ventana_graficar, text="Número de rectángulos:", bg="#f0f0f0").pack(pady=10)
    entry_n = tk.Entry(ventana_graficar, width=10)
    entry_n.pack(pady=5)

    def graficar():
        a, b, c = obtener_coeficientes(entry_a, entry_b, entry_c)
        if a is not None:
            x1 = float(entry_x1.get())
            x2 = float(entry_x2.get())
            n = int(entry_n.get())
            graficar_funcion(a, b, c, x1, x2, n)

    tk.Button(ventana_graficar, text="Graficar", command=graficar, bg="#007acc", fg="white", width=15).pack(pady=20)

def abrir_area_bajo_curva():
    ventana_area = tk.Toplevel(root)
    ventana_area.title("Área Bajo la Curva")
    ventana_area.geometry("400x400")
    ventana_area.resizable(False, False)
    ventana_area.configure(bg="#f0f0f0")

    tk.Label(ventana_area, text="Coeficientes a, b, c:", bg="#f0f0f0").pack(pady=10)

    entry_a = tk.Entry(ventana_area, width=10)
    entry_a.pack(pady=5)
    entry_b = tk.Entry(ventana_area, width=10)
    entry_b.pack(pady=5)
    entry_c = tk.Entry(ventana_area, width=10)
    entry_c.pack(pady=5)

    tk.Label(ventana_area, text="Rango de visualización (x1, x2):", bg="#f0f0f0").pack(pady=10)
    entry_x1 = tk.Entry(ventana_area, width=10)
    entry_x1.pack(pady=5)
    entry_x2 = tk.Entry(ventana_area, width=10)
    entry_x2.pack(pady=5)

    tk.Label(ventana_area, text="Número de rectángulos:", bg="#f0f0f0").pack(pady=10)
    entry_n = tk.Entry(ventana_area, width=10)
    entry_n.pack(pady=5)

    resultado_var = tk.StringVar()
    tk.Label(ventana_area, textvariable=resultado_var, bg="#f0f0f0").pack(pady=10)

    def calcular():
        resultado = calcular_area_rectangulos(entry_a, entry_b, entry_c, entry_x1, entry_x2, entry_n)
        resultado_var.set(resultado)

    tk.Button(ventana_area, text="Calcular", command=calcular, bg="#007acc", fg="white", width=15).pack(pady=20)

def abrir_sistema_ecuaciones():
    ventana_sistema = tk.Toplevel(root)
    ventana_sistema.title("Sistema de Ecuaciones")
    ventana_sistema.geometry("400x400")
    ventana_sistema.resizable(False, False)
    ventana_sistema.configure(bg="#f0f0f0")

    tk.Label(ventana_sistema, text="Matriz de coeficientes (3x3):", bg="#f0f0f0").pack(pady=10)

    matriz_frame = tk.Frame(ventana_sistema, bg="#f0f0f0")
    matriz_frame.pack()

    matriz_entries = []
    for i in range(3):
        fila_entries = []
        for j in range(3):
            entry = tk.Entry(matriz_frame, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            fila_entries.append(entry)
        matriz_entries.append(fila_entries)

    tk.Label(ventana_sistema, text="Vector de resultados (3x1):", bg="#f0f0f0").pack(pady=10)

    vector_frame = tk.Frame(ventana_sistema, bg="#f0f0f0")
    vector_frame.pack()

    vector_entries = []
    for i in range(3):
        entry = tk.Entry(vector_frame, width=5)
        entry.grid(row=i, column=0, padx=5, pady=5)
        vector_entries.append(entry)

    resultado_var = tk.StringVar()
    tk.Label(ventana_sistema, textvariable=resultado_var, bg="#f0f0f0").pack(pady=10)

    def resolver():
        resolver_sistema(matriz_entries, vector_entries, resultado_var)

    tk.Button(ventana_sistema, text="Resolver Sistema", command=resolver, bg="#007acc", fg="white", width=15).pack(pady=20)

def salir():
    root.quit()

# Ventana principal
root = tk.Tk()
root.title("Calculadora de Matemáticas")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Botones
tk.Button(root, text="Resolver Sistema de Ecuaciones", command=abrir_sistema_ecuaciones, bg="#007acc", fg="white", width=30).pack(pady=20)
tk.Button(root, text="Área Bajo la Curva", command=abrir_area_bajo_curva, bg="#007acc", fg="white", width=30).pack(pady=20)
tk.Button(root, text="Graficar Función Cuadrática", command=abrir_graficar_funcion, bg="#007acc", fg="white", width=30).pack(pady=20)
tk.Button(root, text="Salir", command=salir, bg="#d9534f", fg="white", width=30).pack(pady=20)

root.mainloop()