def ordenar_cadenas(lista_cadenas):
    return sorted(lista_cadenas, key=str.lower)

def main():
    lista = []
    print("Ingrese las palabras (ingrese 'listo' para terminar):")
    while True:
        palabra = input()
        if palabra.lower() == 'listo':
            break
        lista.append(palabra)

    lista_ordenada = ordenar_cadenas(lista)
    print("Lista ordenada alfabéticamente:")
    for palabra in lista_ordenada:
        print(palabra)

if __name__ == "__main__":
    main()