perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:

    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for indice, opcao in enumerate(opcoes):
        print(f'{indice})',opcao)
    print()

    escolha = input('Escolha uma opção: ')
    print()

    escolha_int = None
    acertou = False
    qtd_opcoes = len(opcoes)
    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
                
    if acertou:
        qtd_acertos +=1
        print('Acertou')
    else:
        print('Errou')
    print()
print(f'Voçê acertou {qtd_acertos}')
print(f'De {len(pergunta)} perguntas')



