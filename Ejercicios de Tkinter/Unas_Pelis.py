import tkinter as tk

def registrar_peliculas():
    pelicula = entrada_pelicula.get()
    if pelicula:
        lista_pelicula.insert(tk.END, pelicula)
        entrada_pelicula.delete(0, tk.END)

root = tk.Tk()
root.title("Peliculas $v")

etiqueta_titulo = tk.Label(root, text="Escribe el Titulo de una pelicula", font=('Arial', 14))
etiqueta_titulo.pack(pady=10)

entrada_pelicula = tk.Entry(root, font=('Arial', 14))
entrada_pelicula.pack(pady=10, padx=10, fill=tk.X)

boton_registrar = tk.Button(root, text="Registrar pelicula", command=registrar_peliculas, font=('Arial', 14))
boton_registrar.pack(pady=10)

boton_añadir = tk.Button(root, text="Añadir", command=registrar_peliculas, font=('Arial', 14))
boton_añadir.pack(pady=10)

etiqueta_lista = tk.Label(root, text="Peliculas registradas", font=('Arial', 14))
etiqueta_lista.pack(pady=10)

lista_pelicula = tk.Listbox(root, font=('Arial', 14), width=50, height=10)
lista_pelicula.pack(pady=10, padx=10)

root.mainloop()