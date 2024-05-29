def ConvertirEspaciado(texto):
    texto_espacio = ' '.join(texto)
    return texto_espacio
texto = input("Ingrese una frase u/o texto: ")
texto_espacios = ConvertirEspaciado(texto)
print("Texto con espacios adicionales:", texto_espacios)