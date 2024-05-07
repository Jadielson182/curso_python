# Empacotamento  e desempacontamento de dicionários
# a, b = 1, 2
# a, b = b , a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.item()
# print(a1, a2)
# print(b1, b2)

# pessoa = {
#     'nome': 'Aline', 
#     'nome': 'Souza',
# }

# for chave, valor in pessoa.items():
#     print(chave, valor)


# pessoa = {
#     'nome': 'Aline', 
#     'nome': 'Souza',
# }

# dados_pessoa = {
#     'idade': 16,
#     'altura': 1.6,
# }

# pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# #args e kwargs
#args
#kwargs - keyword arguments( argumentos nomeados)


def mostro_argumento_nomeado(*args, **kwargs):
    print('Não nomeados', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumento_nomeado(nome='Joana', qlq=123)
# mostro_argumento_nomeado(**pessoa_completa)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumento_nomeado(3, 'h', 3, **configuracoes)

