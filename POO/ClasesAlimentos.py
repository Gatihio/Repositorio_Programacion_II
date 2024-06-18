from ClasesProductos import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion
        
    def informacion(self):
        super().informacion()
        print("Fecha de expiración:", self.fecha_expiracion)