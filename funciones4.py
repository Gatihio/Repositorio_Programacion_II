def val_intentos(intentos):
    return intentos < 3

def login(usuario, contraseña, intentos):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True, intentos
    else:
        return False, intentos + 1
    
def main():
    intentos = 0
    while val_intentos(intentos):
        usuario = input("Ingrese el nombre del usuario: ")
        contraseña = input("Ingresela contraseña: ")
        acceso, intentos = login(usuario, contraseña, intentos)
        if acceso:
            print("👍, la secion se inicio correctamente")
            break
        else:
            print("El nombre o la contraseña no son correctas")
    else:
        print("Te quedaste sin intentos, ya no podras ingresar")

if __name__ == "__main__":
    main()