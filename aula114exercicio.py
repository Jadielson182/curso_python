#Exercício - Unir listas
#Crie uma função (como o zipper de roupas)
#O trabalho dessa função será unir duas lista na ordem
#Use todos os valores da menor lista
#Ex

# #Resultado
# ['Salvador','Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(lista1, lista2):
    menor = min(len(lista1), len(lista2))
    return [
        (lista1[item], lista2[item])
        for item in range(menor)
    ]

lista1 = ['Salvador','Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(f'{zipper(lista1, lista2)}' )

from itertools import zip_longest

print(list(zip(lista1, lista2)))
print(list(zip_longest(lista1, lista2, fillvalue='SEM CIDADE')))

