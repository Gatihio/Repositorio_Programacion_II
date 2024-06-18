from ClasesProductos import Producto

class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo
    
    def informacion(self):
        super().informacion()
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)