#Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
#que sea la concatenación de ambas.

def concatenar_lista(lista1, lista2):
    lista_concatenada = lista1 + lista2
    return concatenar_lista

lista1 = [43, 65, 23]
lista2 = [12, 87, 1]
lista_concatenada = concatenar_lista(lista1, lista2)
print("Lista concatenada:", lista_concatenada)