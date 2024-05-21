import random

palabras = ["python", "Rubi", "Csharp", "Javascript", "Java", "PHP", "HTLM"]

def seleccionar_palabra(palabras):
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jugar_ahorcado():
    palabra = seleccionar_palabra(palabras)
    intentos_maximos = 6
    intentos = 0
    letras_adivinadas = []
    
    print("¡Bienvenido al Juego de Ahorcado!")
    print("Adivina la palabra:")
    print(mostrar_palabra(palabra, letras_adivinadas))
    
    while intentos < intentos_maximos:
        letra = input("Ingresa una letra: ").lower()
        if letra in letras_adivinadas:
            print("Ya has ingresado esa letra. Intenta con otra.")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
            print(mostrar_palabra(palabra, letras_adivinadas))
            if mostrar_palabra(palabra, letras_adivinadas).replace(" ", "") == palabra:
                print("¡Felicidades! Has adivinado la palabra.")
                break
        else:
            intentos += 1
            print("Incorrecto. Te quedan {} intentos.".format(intentos_maximos - intentos))
    
    if intentos == intentos_maximos:
        print("¡Oh no! Te has quedado sin intentos. La palabra era '{}'.".format(palabra))

jugar_ahorcado()