#Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
#nuevo que invierta las claves y los valores.

def diccionario_invertido(diccionario):
    diccionario_al_reves = {}

    for clave, valor in diccionario.items():
        diccionario_al_reves[valor] = clave

        return diccionario_al_reves
    
    primer_diccionario = {"Ambar": 1, "Beta": 2, "Charli": 3}
    diccionario_al_reves = diccionario_invertido(primer_diccionario)
    print(diccionario_al_reves)