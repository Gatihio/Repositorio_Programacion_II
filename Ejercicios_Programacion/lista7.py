def contar_caracteres(cadena):
    contador = {}
    for caracter in cadena:
        if caracter in contador:
            contador[caracter] += 1
        else:
            contador[caracter] = 1
    return contador

# Ejemplo de uso
cadena_ejemplo = "Hola, ¿cómo estás?"
resultado = contar_caracteres(cadena_ejemplo)
print("Recuento de caracteres en la cadena:")
print(resultado)