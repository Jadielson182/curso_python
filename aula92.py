# def executa(funcao, *args):
#     return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# print(
#     executa(
#         lambda x, y: x + y, 
#         2, 3
#     # ), executa(soma, 2, 3)
# )

# duplica = executa(cria_multiplicador, 2)
# duplica2 = executa(
#     lambda m: lambda n : n * m, 2
# )
# # print(duplica(2))
# print(duplica2(2))

# print(executa( lambda x, y: x + y, 2, 3))

# print(
#     executa(
#         lambda *args: sum(args),
#         1,2,3,4,5,6,7
#     )

# )


produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

# novos_produtos = [
#     {'nome': produto['nome'], 'preco' : produto['preco']}
#     for produto in produtos
# ]
novos_produtos= [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    
    for produto in produtos
]


# print(novos_produtos)
print(*novos_produtos, sep='\n')