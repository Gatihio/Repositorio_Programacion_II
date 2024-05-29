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