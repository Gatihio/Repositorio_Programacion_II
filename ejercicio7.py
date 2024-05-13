import random

print ("Hola, vamos a JUGAR  a un juego")
print ("Tengo unos numeros que van del 1 al 100 y vos vas a tener que saber cual es el correcto")
print ("Empezemos con el juego")

numerito_aleatorio = random.randint(1,100)
verdadero = False

while not verdadero:
    suerte = int(input ("Encuentra el numero entre 1 y 100: "))
    if suerte < numerito_aleatorio:
        print("El número es demasiado bajo, mas para arriba, vos podes.")
    elif suerte > numerito_aleatorio:
        print("Te pasaste un poquito mucho para arriba, pero estas cerca eh.")
    else:
        print("¡Correcto! ¡adivinaste el numero, sos una masa!")
        adivinado = True