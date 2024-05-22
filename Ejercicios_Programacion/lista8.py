import re

def es_palindromo(texto):
    texto_procesado = re.sub(r'[^\w\s]', '', texto.lower().replace(" ", ""))
    return texto_procesado == texto_procesado[::-1]

def main():
    palabra = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")
    if es_palindromo(palabra):
        print(f'"{palabra}" es un palíndromo.')
    else:
        print(f'"{palabra}" no es un palíndromo.')

if __name__ == "__main__":
    main()