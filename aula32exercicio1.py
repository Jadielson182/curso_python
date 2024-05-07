'''numero = input('Digite um numero inteiro: ')
if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    elif numero % 2 == 1:
        print(f'O número {numero} é impar.')
else:
    print(f'{numero} não e um numero inteiro.')'''

numero = input('Digite um numero inteiro: ')

if numero.isdigit(): #poderia remover if e botar try e removert else e botar except
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar is True:
        par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}.')
else:
    print('Voçê não digitou um número inteiro.')