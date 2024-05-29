#Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
#con la frecuencia de cada letra en la cadena.

def contador_letras(cadena):
    frecuencia_letras = {}

    for letras in cadena:
        if letras !='':
            if letras in frecuencia_letras:
                frecuencia_letras[letras] += 1
            else:
                frecuencia_letras[letras] + 1

    return frecuencia_letras
            
cadena = "No jota por hay no"
resultado = contador_letras(cadena)
print(resultado)