contraseña = input("Ingrese una contraseña valida")
mayusculas = 0
minusculas = 0
caracteresp = 0
if contraseña.__len__ >= 8 and contraseña.__len__() <= 20:
    while contraseña.__len__() < 21:
        if search["A-Z"]:
            mayusculas += 1
        elif search["a-z"]:
            minusculas += 1
        elif search["1-1000"] and ["!,@,#,$,%,/,-"]:
            caracteresp += 1
    contraseña + 1
else:
    print("contraseña no valida, cumpla con las condiciones")
    print("debe contener al menos 1 caracter en Mayuscula y 1 en minuscula")
    print("Al menos un numero o un caracter especial")

print("Contraseña valida !")