import math
import statistics
from tabulate import tabulate
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel

# Funciones para la gráfica y área bajo la curva
def graficar_funcion(a, b, c, x1, x2):
    x = np.linspace(x1, x2, 400)
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

def obtener_coeficientes():
    while True:
        try:
            coef_str = simpledialog.askstring("Coeficientes", "Ingrese los coeficientes (a, b, c) separados por espacios:")
            return tuple(map(float, coef_str.split()))
        except ValueError:
            messagebox.showerror("Error", "Entrada no válida. Intente de nuevo.")

def calcular_area_rectangulos(a, b, c, a_intervalo, b_intervalo, n):
    def f(x):
        return a * x**2 + b * x + c

    dx = (b_intervalo - a_intervalo) / n
    suma_inferior = sum(f(a_intervalo + i * dx) * dx for i in range(n))
    suma_superior = sum(f(a_intervalo + (i + 1) * dx) * dx for i in range(n))

    x_values = np.linspace(a_intervalo, b_intervalo, 1000)
    y_values = f(x_values)
    area_real = np.trapz(y_values, x_values)

    return suma_inferior, suma_superior, area_real

# Funciones para distribuciones
def distribucion_binomial(n, p, k):
    from math import comb
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def distribucion_poisson(lambd, k):
    from math import exp, factorial
    return (exp(-lambd) * (lambd ** k)) / factorial(k)

def distribucion_hipergeometrica(n, M, N, k):
    from math import comb
    return (comb(M, k) * comb(N - M, n - k)) / comb(N, n)

def distribucion_normal(x, mu, sigma):
    return norm.cdf(x, mu, sigma)

def distribucion_normal_intervalo(x1, x2, mu, sigma):
    return norm.cdf(x2, mu, sigma) - norm.cdf(x1, mu, sigma)

# Clase principal de la aplicación
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación Estadística")
        self.geometry("400x400")
        self.lista = []

        # Menú principal
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Seleccione una opción:", font=("Arial", 14)).pack(pady=10)

        tk.Button(self, text="Agregar Elementos", command=self.agregar_elementos).pack(pady=5)
        tk.Button(self, text="Medidas de Posición", command=self.medidas_posicion).pack(pady=5)
        tk.Button(self, text="Funciones Estadísticas", command=self.funciones_estadisticas).pack(pady=5)
        tk.Button(self, text="Distribuciones", command=self.distribuciones).pack(pady=5)
        tk.Button(self, text="Gráfica Función Cuadrática", command=self.graficar_funcion).pack(pady=5)
        tk.Button(self, text="Resolver Sistema de Ecuaciones", command=self.resolver_ecuaciones).pack(pady=5)
        tk.Button(self, text="Calcular Área Bajo la Curva", command=self.calcular_area_bajo_curva).pack(pady=5)
        tk.Button(self, text="Salir", command=self.quit).pack(pady=20)

    def agregar_elementos(self):
        self.lista_window = Toplevel(self)
        self.lista_window.title("Agregar Elementos")
        tk.Label(self.lista_window, text="Ingrese los datos uno por uno. Presione 'Agregar' para agregar y 'Finalizar' para terminar.").pack(pady=10)

        self.entry = tk.Entry(self.lista_window)
        self.entry.pack(pady=5)

        tk.Button(self.lista_window, text="Agregar", command=self.agregar_elemento).pack(pady=5)
        tk.Button(self.lista_window, text="Finalizar", command=self.finalizar_agregar).pack(pady=5)

    def agregar_elemento(self):
        valor = self.entry.get()
        if valor:
            try:
                self.lista.append(float(valor))
                self.entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Entrada no válida.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un valor.")

    def finalizar_agregar(self):
        self.lista.sort()
        self.lista_window.destroy()
        messagebox.showinfo("Información", "Elementos agregados correctamente.")

    def medidas_posicion(self):
        if not self.lista:
            messagebox.showinfo("Error", "La lista está vacía.")
            return

        media = sum(self.lista) / len(self.lista)
        mediana = statistics.median(self.lista)
        moda = statistics.mode(self.lista)
        q1, mediana, q3 = np.percentile(self.lista, [25, 50, 75])
        desvio = np.std(self.lista, ddof=1)

        resultados = (
            f"Media: {media}\n"
            f"Mediana: {mediana}\n"
            f"Moda: {moda}\n"
            f"Cuartiles: Q1={q1}, Mediana={mediana}, Q3={q3}\n"
            f"Desviación Estándar: {desvio}"
        )
        messagebox.showinfo("Medidas de Posición", resultados)

    def funciones_estadisticas(self):
        if not self.lista:
            messagebox.showinfo("Error", "La lista está vacía.")
            return

        frec_abs = {elem: self.lista.count(elem) for elem in set(self.lista)}
        frec_rel = {elem: round(freq / len(self.lista), 4) for elem, freq in frec_abs.items()}
        frec_abs_acum = {elem: sum(frec_abs[k] for k in sorted(frec_abs) if k <= elem) for elem in sorted(frec_abs)}
        frec_rel_acum = {elem: round(sum(frec_rel[k] for k in sorted(frec_rel) if k <= elem), 2) for elem in sorted(frec_rel)}

        resultados = (
            f"Frecuencia Absoluta:\n{frec_abs}\n"
            f"Frecuencia Relativa:\n{frec_rel}\n"
            f"Frecuencia Absoluta Acumulada:\n{frec_abs_acum}\n"
            f"Frecuencia Relativa Acumulada:\n{frec_rel_acum}"
        )
        messagebox.showinfo("Funciones Estadísticas", resultados)

    def graficar_funcion(self):
        a, b, c = obtener_coeficientes()
        x1 = simpledialog.askfloat("Rango", "Ingrese x1:")
        x2 = simpledialog.askfloat("Rango", "Ingrese x2:")
        if x1 is not None and x2 is not None:
            graficar_funcion(a, b, c, x1, x2)

    def resolver_ecuaciones(self):
        # Método simple para resolver un sistema de ecuaciones 2x2
        try:
            eq1 = simpledialog.askstring("Ecuación 1", "Ingrese la primera ecuación (ejemplo: '2x + 3y = 5'):")
            eq2 = simpledialog.askstring("Ecuación 2", "Ingrese la segunda ecuación (ejemplo: 'x - 2y = 1'):")
            # Procesamiento simplificado
            # Aquí se puede mejorar la lógica para resolver ecuaciones
            # usando `sympy` o un método específico
            messagebox.showinfo("Resultado", "Funcionalidad de resolución de ecuaciones aún no implementada.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_area_bajo_curva(self):
        a, b, c = obtener_coeficientes()
        a_intervalo = simpledialog.askfloat("Intervalo", "Ingrese el límite inferior:")
        b_intervalo = simpledialog.askfloat("Intervalo", "Ingrese el límite superior:")
        n = simpledialog.askinteger("Cantidad de Rectángulos", "Ingrese la cantidad de rectángulos:")

        if None not in (a_intervalo, b_intervalo, n):
            suma_inferior, suma_superior, area_real = calcular_area_rectangulos(a, b, c, a_intervalo, b_intervalo, n)
            resultados = (
                f"Área inferior: {suma_inferior}\n"
                f"Área superior: {suma_superior}\n"
                f"Área real: {area_real}"
            )
            messagebox.showinfo("Área Bajo la Curva", resultados)
        else:
            messagebox.showwarning("Advertencia", "Se deben ingresar todos los valores.")

    def distribuciones(self):
        self.distribucion_window = Toplevel(self)
        self.distribucion_window.title("Distribuciones")

        tk.Label(self.distribucion_window, text="Seleccione tipo de distribución:").pack(pady=10)

        tk.Button(self.distribucion_window, text="Binomial", command=self.distribucion_binomial).pack(pady=5)
        tk.Button(self.distribucion_window, text="Poisson", command=self.distribucion_poisson).pack(pady=5)
        tk.Button(self.distribucion_window, text="Hipergeométrica", command=self.distribucion_hipergeometrica).pack(pady=5)
        tk.Button(self.distribucion_window, text="Normal", command=self.distribucion_normal).pack(pady=5)

    def distribucion_binomial(self):
        n = simpledialog.askinteger("Distribución Binomial", "Ingrese n:")
        p = simpledialog.askfloat("Distribución Binomial", "Ingrese p:")
        k = simpledialog.askinteger("Distribución Binomial", "Ingrese k:")
        resultado = distribucion_binomial(n, p, k)
        messagebox.showinfo("Resultado Binomial", f"P(X={k}) = {resultado}")

    def distribucion_poisson(self):
        lambd = simpledialog.askfloat("Distribución Poisson", "Ingrese λ:")
        k = simpledialog.askinteger("Distribución Poisson", "Ingrese k:")
        resultado = distribucion_poisson(lambd, k)
        messagebox.showinfo("Resultado Poisson", f"P(X={k}) = {resultado}")

    def distribucion_hipergeometrica(self):
        n = simpledialog.askinteger("Distribución Hipergeométrica", "Ingrese n:")
        M = simpledialog.askinteger("Distribución Hipergeométrica", "Ingrese M:")
        N = simpledialog.askinteger("Distribución Hipergeométrica", "Ingrese N:")
        k = simpledialog.askinteger("Distribución Hipergeométrica", "Ingrese k:")
        resultado = distribucion_hipergeometrica(n, M, N, k)
        messagebox.showinfo("Resultado Hipergeométrica", f"P(X={k}) = {resultado}")

    def distribucion_normal(self):
        mu = simpledialog.askfloat("Distribución Normal", "Ingrese la media (μ):")
        sigma = simpledialog.askfloat("Distribución Normal", "Ingrese la desviación estándar (σ):")
        x = simpledialog.askfloat("Distribución Normal", "Ingrese x:")
        resultado = distribucion_normal(x, mu, sigma)
        messagebox.showinfo("Resultado Normal", f"P(X<={x}) = {resultado}")

# Ejecución de la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
