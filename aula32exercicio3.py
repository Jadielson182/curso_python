'''nome = input('Digite Seu nome: ')
nome = str(nome)
if len(nome) <= 4:
    print('Seu nome e curto.')
elif len(nome) == 5 or len(nome ) == 6:
    print('Seu nome e normal.')
elif len(nome) > 6 :
    print('Seu nome e muito grande.')'''


nome = input('Digite Seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome e normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')