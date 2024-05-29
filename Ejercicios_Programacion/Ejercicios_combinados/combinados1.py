#Notas de estudiantes : Escribe una función que recibe un diccionario donde las claves son nombres de estudiantes y los valores son listas de sus calificaciones. 
#La función debe devolver un nuevo diccionario con las mismas claves pero donde los valores son la calificación promedio de cada estudiante.

def clave_estudiantes(diccionario):
    clave_nombre = {}

    for clave in diccionario:
        if clave not in clave_nombre:
            clave_nombre[clave] = diccionario[clave]
            suma = sum(diccionario[clave]) 
            promedio = suma / len(diccionario[clave])
            clave_nombre[clave] = promedio

    return clave_nombre

nombre_estudiantes = {
"saul": [7, 8, 4],
"pucheta": [1, 2, 3]
}

resultado = clave_estudiantes(nombre_estudiantes)
print(resultado)