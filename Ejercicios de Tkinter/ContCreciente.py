import tkinter as tk

# Función para incrementar el contador y actualizar la etiqueta
def incrementar_contador():
    global contador
    contador += 1
    etiqueta_contador.config(text=f"Contador: {contador}")

root = tk.Tk()
root.title("Contador creciente")

# Crear un marco
marco = tk.Frame(root, bg="lightblue", padx=10, pady=10)
marco.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

contador = 0

# Crear una etiqueta para mostrar el contador
etiqueta_contador = tk.Label(marco, text=f"Contador: {contador}", font=("Arial", 16), bg="lightblue")
etiqueta_contador.pack(pady=10)

# Agregar un nombre o título al marco usando una etiqueta
nombre_marcado = tk.Label(marco, text="Contador Creciente", bg="lightblue", font=("Arial", 14, "bold"))
nombre_marcado.pack(pady=(0, 10))

# Crear un botón con el símbolo + y una acción
boton_mas = tk.Button(marco, text="+", font=("Arial", 24), width=5, height=2, command=incrementar_contador)
boton_mas.pack(pady=10)

# Agregar un widget dentro del marco
etiqueta = tk.Label(marco, text="¡Hata cuanto podes llegar!", bg="lightblue")
etiqueta.pack()

# Ejecutar el bucle principal
root.mainloop()
