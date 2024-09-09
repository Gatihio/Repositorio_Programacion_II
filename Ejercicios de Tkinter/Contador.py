import tkinter as tk

def Count_up():
    current_value = int(contador.get())
    contador.set(str(current_value + 1))

def Count_down():
    current_value = int(contador.get())
    if current_value > 0:
        contador.set(str(current_value - 1))

def Count_reset():
    contador.set("0")

root = tk.Tk()
root.title("Contador")

root = tk.Frame(root, bg="lightblue", padx=10, pady=10)
root.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

etiqueta_contador = tk.Label(root, text="Contador")
etiqueta_contador.pack(pady=10)

contador = tk.StringVar()
contador.set("0")

entrada_contador = tk.Entry(root, textvariable=contador, state='readonly', font=('Arial', 14))
entrada_contador.pack(pady=10)

boton_Cont_up = tk.Button(root, text="Count Up", font=("Arial", 15), width=5, height=2, command=Count_up)
boton_Cont_up.pack(side=tk.LEFT, padx=5,pady=10)

boton_Cont_down = tk.Button(root, text="Count Down", font=("Arial", 15), width=5, height=2, command=Count_down)
boton_Cont_down.pack(side=tk.LEFT, padx=5,pady=10)

boton_reset = tk.Button(root, text="Reset", font=("Arial", 15), width=5, height=2, command=Count_reset)
boton_reset.pack(side=tk.LEFT, padx=5,pady=10)

root.mainloop()