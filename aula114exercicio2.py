"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
# """

def soma_lista(lista1, lista2):
    menor = min(len(lista1), len(lista2))
    return [lista1[indice] + lista2[indice]
        for indice in range(menor)

    ]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print(soma_lista(lista_a, lista_b))

# Outro forma de fazer
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

menor = min(len(lista_a),len(lista_b))

nova_lista =[lista_a[indice] + lista_b[indice] for indice in range(menor)]

print(nova_lista)
#Outra forma
nova_lista = []
menor = min(len(lista_a),len(lista_b))
for indice in range(menor):
    nova_lista.append(lista_a[indice] + lista_b[indice])

print(nova_lista)
# Outra forma

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

nova_lista = [(a + b) for a, b in zip(lista_a, lista_b)]
print(nova_lista)

#Outra forma

nova_lista = []
for indice, _ in enumerate(lista_b):
    nova_lista.append(lista_a[indice] + lista_b[indice])

print(nova_lista)