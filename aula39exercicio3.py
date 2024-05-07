#          '''Calculadora com while'''   
txt = 'CALCULADORA'
print('=' * 40)
print(f'{txt: ^40}')
print('=' * 40)
while True:
    calculadora = input('Digite a operação (soma, sub, mult, div): ').lower()
    valor_1 = input('Digite um numero: ')
    valor_2 = input('Digite outro valor: ')
    if calculadora == 'soma':
        soma = int(valor_1) + int(valor_2)
        print(f'A soma de {valor_1} + {valor_2} é {soma}')
    if calculadora == 'sub':
       subtraçao= int(valor_1) - int(valor_2)
       print(f'A subtração de {valor_1} - {valor_2} é {subtraçao}')
    if calculadora == 'mult':
        multiplicaçao = int(valor_1) * int(valor_2)
        print(f'A multiplicação de {valor_1} * {valor_2} é {multiplicaçao}')
    if calculadora == 'div':
        divisao = int(valor_1) / int(valor_2)
        print(f'A divisão de {valor_1} / {valor_2} é {divisao}')
    sair = input('Quer sair [s]sim: ').lower().startswith('s')
    if sair is True:
        break     
print('Encerrando a calculadora')
