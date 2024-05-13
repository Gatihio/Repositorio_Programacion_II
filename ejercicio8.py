import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation

longitud_contraseña = 12
contraseña = ''.join(random.choice(caracteres) for _ in range(longitud_contraseña))

print("La contraseña que fue generarda con caracteres aleatorios es: ", contraseña)