#Exercício
nome = (input('Digite seu nome: '))
idade = (input('Digite sua idade: '))
if nome == '' and idade == '': 
    print('Desculpa, voçê deixou camos vazios.')
if nome != '' or idade != '': # poderia usar if nome and idade, que seia verdadeira e verdadeira
    print(f'Seu nome é {nome} e sua idade é {idade} anos.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    if ' ' in nome:
        print(f'Seu nome contém espaços.')
    if' ' not in nome:
        print('Seu nome não tem espãos.')
    print(f'Seu nome tem {len(nome)} caractere.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')


#Resposta do curso

'''
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")'''


