#Invertir lista: Escribe una función que tome una lista y devuelva una nueva lista con los
#elementos en orden inverso.

def dar_vueelta_lista(lista):
    dar_vueelta_lista = lista[::-1]
    return dar_vueelta_lista

numeros = [1, 2, 3, 4, 5]
lista_invertida = dar_vueelta_lista(numeros)
print("Lista invertida:", lista_invertida)