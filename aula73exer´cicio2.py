def ParOuÍmpar(num):
    if num % 2 == 0:
        return f'O número {num} é Par'
    elif num % 2 == 1:
        return f'O número {num} é Ímpar'



numero = int(input('Digite um numero: '))
resposta = ParOuÍmpar(numero)
print(resposta)


# def par_impar(num):
#     multiplo_de_dois = num % 2 == 0
#     if multiplo_de_dois:
#         return f'{num} é par'
#     return f'{num} é ímpar'


# print(par_impar(2))
# print(par_impar(3))
# print(par_impar(7))
# print(par_impar(15))
# print(par_impar(16))