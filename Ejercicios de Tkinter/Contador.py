import tkinter as tk

def incrementar_contador():
    global contador
    contador += 1
    etiqueta_contador.config(text=f"Contador: {contador}")

root = tk.Tk()
root.title("Contador")

contador = 0

etiqueta_contador = tk.Label(root, text=f"Contador: {contador}", font=("Arial", 16), bg="lightblue")
etiqueta_contador.pack(pady=10)

marco = tk.Frame(root, bg="lightblue", padx=10, pady=10)
marco.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

nombre_marcado = tk.Label(marco, text="Contador", bg="lightblue", font=("Arial", 14, "bold"))
nombre_marcado.pack(pady=(0, 10))

# Crear las etiquetas
etiqueta_contup = tk.Label(root, text="ContUp")
etiqueta_contdown = tk.Label(root, text="ContDown")
etiqueta_reset = tk.Label(root, text="Reset")

etiqueta_contup.grid(row=0, column=0, padx=10, pady=5, sticky='e')
etiqueta_contdown.grid(row=1, column=0, padx=10, pady=5, sticky='e')
etiqueta_reset.grid(row=2, column=0, padx=10, pady=5, sticky='e')

entrada_contup = tk.Entry(marco, state='readonly') 
entrada_contdown = tk.Entry(marco, state='readonly') 
entrada_reset = tk.Entry(marco, state='readonly') 

etiqueta_contup.grid(row=0, column=0, padx=10, pady=5, sticky='e')
entrada_contup.grid(row=0, column=1, padx=10, pady=5)
etiqueta_contdown.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entrada_contdown.grid(row=1, column=1, padx=10, pady=5)
etiqueta_reset.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entrada_reset.grid(row=2, column=1, padx=10, pady=5)


root.mainloop()