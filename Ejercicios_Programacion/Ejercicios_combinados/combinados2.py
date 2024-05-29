#Palabras por letra inicial : Escribe una función que tome una lista de palabras y devuelva un diccionario donde las claves son las 
#letras iniciales de las palabras y los valores son listas de palabras que comienzan con esa letra.

def lista_palabras(lista):
    letras_iniciales = {}

    for palabras in lista:
        inicial = palabras[0]
        if inicial not letras_iniciales