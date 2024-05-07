# Dictionary Comprehension e set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio'
}
# print(produto.items())

# for chave, valor in produto.items():
#     print(chave, valor)


dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'

}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a')
]
# dc = {
#     chave: valor
#     for chave, valor in lista
# }

# print(dict(lista))

s1 = {2 ** i  for i in range(10)}
print(s1)


