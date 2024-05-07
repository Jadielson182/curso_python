# List comprehension em python: tudo o que voçê precisa saber parte 4

string = 'Otávio Miranda'

numeros_de_letras = 1

# nova_string = ''.join([letra for letra in string])

nova_string = '.'.join([
     string[indice:indice + numeros_de_letras]
     for indice in range(0, len(string), numeros_de_letras)])
print(nova_string)