import pprint


def pp(valor):
    pprint.pprint(valor, sort_dicts=False, width= 80)


produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {'nome': produto['nome'], 'preco' : produto['preco']}
    for produto in produtos
]
novos_produtos= [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]


# print(novos_produtos)
print(*novos_produtos, sep='\n')
# pprint.pprint(novos_produtos, sort_dicts=False, width=80)

# pp(novos_produtos)

# lista = [n for n in range(10) if n > 5]

novos_produtos= [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos 
    if (produto['preco'] > 20 and produto['preco'] * 1.05) > 10 
]



pp(novos_produtos)