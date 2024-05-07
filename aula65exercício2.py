# Gerador de CPF
import random
for _ in range(20):
    nove_digitos = ''
    for numero in range(0, 9):
        nove_digitos += str(random.randint(0, 9))
    contador_regressivo_1 = 10
    soma_primeiro_digito = 0
    for digito in nove_digitos:
        digito = int(digito)
        soma_primeiro_digito += digito * contador_regressivo_1
        contador_regressivo_1 -= 1

    primeiro_digito = (soma_primeiro_digito * 10) % 11
    primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito
    #calculo do segundo digito
    dez_digitos =  nove_digitos + str(primeiro_digito)
    contador_regressivo_2 = 11
    soma_segundo_digito = 0

    for digito in dez_digitos:
        digito = int(digito)
        soma_segundo_digito += digito * contador_regressivo_2
        contador_regressivo_2 -= 1

    segundo_digito = (soma_segundo_digito * 10) % 11
    segundo_digito = 0 if segundo_digito > 9 else segundo_digito

    novo_cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
    print(novo_cpf_gerado)