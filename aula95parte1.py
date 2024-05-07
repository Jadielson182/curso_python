# List comprehension em python: tudo o que voçê precisa saber


# numeros = [1, 2, 3, 4, 5]
# novos_numeros = [numero for numero in numeros]

# # novos_numeros = []
# # for numero in numeros:
# #     novos_numeros.append(numero)

# numeros[0] = 20
# print(novos_numeros)


# numeros = [1, 2, 3, 4, 5]
# divisao= [numero / 2 for numero in numeros]
# multiplicaçao = [numero * 2 for numero in numeros]
# quadrado = [numero ** 2 for numero in numeros]

# print(numeros)
# print(divisao)
# print(multiplicaçao)
# print(quadrado)


def divisãofn(x, y):
    return x / y


def multiplicaçãofn(x, y):
    return x * y


def potenciaçãofn(x, y):
    return x ** y

numeros = [1, 2, 3, 4, 5]
divisao= [divisãofn(numero, 2) for numero in numeros]
multiplicaçao = [multiplicaçãofn(numero, 2) for numero in numeros]
quadrado = [potenciaçãofn(numero, 2) for numero in numeros]


print(numeros)
print(divisao)
print(multiplicaçao)
print(quadrado)
