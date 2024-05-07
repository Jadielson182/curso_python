primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
# if primeiro_valor > segundo_valor:
#     print(f'O primeiro valor {primeiro_valor} e maior que o segundo  valor que é {segundo_valor}.a')
# elif primeiro_valor < segundo_valor:
#     print(f'O segundo valor que é {segundo_valor} e maior que o primeiro valor que é {primeiro_valor}.')
# elif primeiro_valor == segundo_valor:
#     print(f'O primeiro valor {primeiro_valor} tem o mesmo valor que o segundo valor que é {segundo_valor}.')
# print('Fim')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior '
        f'do que  {segundo_valor=} '
    )
elif segundo_valor > primeiro_valor:
    print(
        f'{segundo_valor=} é maior '
        f'do que {segundo_valor=}'
    )
elif primeiro_valor == segundo_valor:
    print(
        f'O {primeiro_valor=} tem o mesmo valor '
        f'que {segundo_valor=}'
    )
print('FIM')