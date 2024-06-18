class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def informacion(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad disponible:", self.cantidad)