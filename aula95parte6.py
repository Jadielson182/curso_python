# List comprehension em python: tudo o que voçê precisa saber parte 6

numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)