#Exercício  total * I / 100
# Aumente o preço dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (copia profunda)
import copy
produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},                  #poderia bota lista em outro modulo e char so variavel
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]
copia_dos_produtos = copy.deepcopy(produtos)
novos_produtos = [
    {**produto, 'preco':round(produto['preco'] * 1.1, 2)}
    for produto in copia_dos_produtos 
]
for produto in novos_produtos:
    print(produto)
print()
print()

def ordena_nome(item):  # poderia ser usadas demodulos 
    return item['nome']


def ordena_preco(item):
    return item['preco']



produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=ordena_nome, reverse=True) # ou key=lambda produto: produto['nome'] depois so da print
 
for item in produtos_ordenados_por_nome:
    print(item)
print() 
print()
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=ordena_preco)# ou key=lambda produto: produto['preco'] depois so da print


for item in produtos_ordenados_por_preco:
    print(item)



