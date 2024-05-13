<<<<<<< HEAD
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
=======
import re
def vai_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not re.search (r"[A-Z]", contraseña):
        return False
    if not re.search (r"[a-z]", contraseña):
        return False
    if not re.search (r"\d", contraseña):
        return False
    if not re.search (r"[!@#$%^&*]", contraseña):
        return False
    return True
def main():
    contraseña = input ("Ingrese su contraseña: ")
    if vai_contraseña (contraseña):
        print ("La contraseña es valida.")
    else:
        print ("La contraseña no es valida, intentelo de nuevo.")
if __name__ == "__main__":
    main()
>>>>>>> 31ff8fda05d77fb63ea133c7ee8ab4e98d55cf6a
