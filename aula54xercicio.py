"""
Exrcício
xiba os índices da lista
0 Maria
1 Hlena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz',]
lista.append(True)
lista.append('jadielson')
lista.append(1.2)
lista.append(10)
lista.append(12)
indices = range(0, len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
print(indices)

# for nome in range(0, len(lista)):
    # print(nome)