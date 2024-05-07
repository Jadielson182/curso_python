# Exercício - sistema de perguntas e resposta

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
acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print('=' * 20)

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print('=' * 20)

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    quantidade_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < quantidade_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print('=' * 20)

    if acertou:
        acertos +=1
        print('Acertou')
    else:
        print('Errou')
    
    print('Voçê acertou ', acertos)
    print('de', len(perguntas), 'perguntas.')