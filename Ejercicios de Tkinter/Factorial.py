import tkinter as tk
from math import factorial

def validar_numeros(char):
    return char.isdigit() or char == ""

def calcular_factorial():
    try:
        numero = int(entrada_numerica_x.get())
        
        resultado = factorial(numero)
        
        entrada_numerica_xx.delete(0, tk.END)  
        entrada_numerica_xx.insert(0, str(resultado))  
    except ValueError:
        entrada_numerica_xx.delete(0, tk.END)  #
        entrada_numerica_xx.insert(0, "Error")  
root = tk.Tk()
root.title("Factorial")

def siguiente():
    print("Botón Siguiente presionado")

root = tk.Tk()
root.title("Entradas Numéricas y Etiquetas")

marco = tk.Frame(root, bg="lightblue", padx=10, pady=10)
marco.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

etiqueta_x = tk.Label(marco, text="n", font=("Arial", 16), bg="lightblue")
etiqueta_x.grid(row=0, column=0, padx=10, pady=5)  

validar_cmd = root.register(validar_numeros)
entrada_numerica_x = tk.Entry(marco, font=("Arial", 16), bg="white", validate="key", validatecommand=(validar_cmd, "%S"))
entrada_numerica_x.grid(row=0, column=1, padx=10, pady=5) 

etiqueta_derecha_x = tk.Label(marco, text="Etiqueta 1", font=("Arial", 16), bg="lightblue")
etiqueta_derecha_x.grid(row=0, column=2, padx=10, pady=5) 

etiqueta_xx = tk.Label(marco, text="Factorial(n)", font=("Arial", 16), bg="lightblue")
etiqueta_xx.grid(row=1, column=0, padx=10, pady=5) 

entrada_numerica_xx = tk.Entry(marco, font=("Arial", 16), bg="white", state='readonly')  # `state='readonly'` para hacerlo no editable
entrada_numerica_xx.grid(row=1, column=1, padx=10, pady=5)

etiqueta_derecha_xx = tk.Label(marco, text="Etiqueta 2", font=("Arial", 16), bg="lightblue")
etiqueta_derecha_xx.grid(row=1, column=2, padx=10, pady=5)  

boton_siguiente = tk.Button(marco, text="Siguiente", font=("Arial", 16), command=siguiente)
boton_siguiente.grid(row=2, column=0, columnspan=3, pady=10)  


root.mainloop()