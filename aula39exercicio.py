
# nome = input('Digite seu nome: ')
# tamanho_nome = len(nome)
# nome_2 = ''
# contador = 0
# while contador < tamanho_nome:  
#     print(f'{contador} = {nome[contador]} ', end=' , ')
#     nome_2 += nome[contador]
#     contador +=1
# print(f' = {nome_2}')

nome = 'Luis Otávio'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1
print(novo_nome)