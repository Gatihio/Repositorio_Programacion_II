import tkinter as tk

def calcular():
    try:
        valor1 = float(entrada_valor1.get())
        valor2 = float(entrada_valor2.get())
        operacion = var.get()
        
        if operacion == "Suma":
            resultado = valor1 + valor2
        elif operacion == "Resta":
            resultado = valor1 - valor2
        elif operacion == "Multiplicación":
            resultado = valor1 * valor2
        elif operacion == "División":
            if valor2 != 0:
                resultado = valor1 / valor2
            else:
                resultado = "Error: División por 0"
        else:
            resultado = "Seleccione una operación"
        
        entrada_resultado.config(state='normal')  
        entrada_resultado.delete(0, tk.END)  
        entrada_resultado.insert(0, str(resultado))  
        entrada_resultado.config(state='readonly')  
    
    except ValueError:
        entrada_resultado.config(state='normal')
        entrada_resultado.delete(0, tk.END)
        entrada_resultado.insert(0, "Error: Valor inválido")
        entrada_resultado.config(state='readonly')

# Función que se llama cuando cambia la opción seleccionada
def mostrar_opcion():
    seleccion = var.get()
    print(f'Opción seleccionada: {seleccion}')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora 2")

# Variable que almacenará el valor seleccionado por los botones de opción
var = tk.StringVar(value="")

# Crear las etiquetas
etiqueta_valor1 = tk.Label(ventana, text="Valor 1:")
etiqueta_valor2 = tk.Label(ventana, text="Valor 2:")
etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_operacion = tk.Label(ventana, text="Operación:")

# Ubicar las etiquetas en la ventana
etiqueta_valor1.grid(row=0, column=0, padx=10, pady=5, sticky='e')
etiqueta_valor2.grid(row=1, column=0, padx=10, pady=5, sticky='e')
etiqueta_resultado.grid(row=2, column=0, padx=10, pady=5, sticky='e')
etiqueta_operacion.grid(row=3, column=0, padx=10, pady=5, sticky='e')

# Crear los campos de entrada
entrada_valor1 = tk.Entry(ventana)
entrada_valor2 = tk.Entry(ventana)
entrada_resultado = tk.Entry(ventana, state='readonly') 

# Ubicar los campos de entrada usando grid
etiqueta_valor1.grid(row=0, column=0, padx=10, pady=5, sticky='e')
entrada_valor1.grid(row=0, column=1, padx=10, pady=5)
etiqueta_valor2.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entrada_valor2.grid(row=1, column=1, padx=10, pady=5)
etiqueta_resultado.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entrada_resultado.grid(row=2, column=1, padx=10, pady=5)

# Ubicar la etiqueta de operación y los botones de opción usando grid
etiqueta_operacion.grid(row=3, column=0, padx=10, pady=5, sticky='e')
rb_suma = tk.Radiobutton(ventana, text="Suma", variable=var, value="Suma")
rb_resta = tk.Radiobutton(ventana, text="Resta", variable=var, value="Resta")
rb_multiplicacion = tk.Radiobutton(ventana, text="Multiplicación", variable=var, value="Multiplicación")
rb_division = tk.Radiobutton(ventana, text="División", variable=var, value="División")

# Crear los botones de opción
rb_suma = tk.Radiobutton(ventana, text="Suma", variable=var, value="Suma", command=mostrar_opcion)
rb_resta = tk.Radiobutton(ventana, text="Resta", variable=var, value="Resta", command=mostrar_opcion)
rb_multiplicacion = tk.Radiobutton(ventana, text="Multiplicación", variable=var, value="Multiplicación", command=mostrar_opcion)
rb_division = tk.Radiobutton(ventana, text="División", variable=var, value="División", command=mostrar_opcion)

# Ubicar los botones de opción en la ventana
rb_suma.grid(row=3, column=1, padx=10, pady=5, sticky='w')
rb_resta.grid(row=4, column=1, padx=10, pady=5, sticky='w')
rb_multiplicacion.grid(row=5, column=1, padx=10, pady=5, sticky='w')
rb_division.grid(row=6, column=1, padx=10, pady=5, sticky='w')

# Crear el botón de calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)

# Ubicar el botón de calcular usando grid
boton_calcular.grid(row=7, column=1, padx=10, pady=10, sticky='w')

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
