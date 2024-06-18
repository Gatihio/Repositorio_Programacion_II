from ClasesElectronicos import Electronico
from ClasesAlimentos import Alimento

producto_electronico = Electronico("Televisor", "$300", 10, "Philips", "LCD9000")
producto_alimenticio = Alimento("Milanesa", "$13.99", 4, "2024-06-11")

print("Información del producto electrónico: ")
producto_electronico.informacion()

print("------------------------------------------")

print("Información del producto alimenticio: ")
producto_alimenticio.informacion()