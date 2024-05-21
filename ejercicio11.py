def juego_adivina_numero():
    print("Piensa en un número entre 1 y 100.")
    input("Cuando estes listo para jugar presiona enter")
    
    limite_inferior = 1
    limite_superior = 100
    adivinado = False
    
    while not adivinado:
        intento = (limite_inferior + limite_superior) // 2
        print("¿Es {} tu número?".format(intento))
        respuesta = input("Ingresa 'menor', 'mayor' o 'igual': ").lower()
        
        if respuesta == "igual":
            print("Adivinaste, sos una locura.")
            adivinado = True
        elif respuesta == "menor":
            limite_superior = intento - 1
        elif respuesta == "mayor":
            limite_inferior = intento + 1
        else:
            print("Por favor, ingresa una respuesta válida.")
    
juego_adivina_numero()