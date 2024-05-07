cpf = '85618175002'# Gerador de cpf

#calculo do primeiro digito
import re # importa o sub para substituir
import sys # importa o exit
entrada = input('Digite o CPF: ')
# cpf_enviado_usuario = '344.950.830-07'\
#     .replace('.','') \
#     .replace('-', '')
cpf_enviado_usuario = re.sub(
    r'[^0-9]', '' ,    #vai substituir tudo que nao for um numero de 0 a 9 pelo que vem depois da virgula (r[^0-9] ,'', )
    # '344.950.830-07'
    entrada
) 
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:  # se a entrada for sequencial, ou seja, caractere repetidos e um bool Tru ou False
    print('Vo~e enviou números sequenciais que não pode forma um CPF.')
    sys.exit()


nove_digitos = cpf_enviado_usuario [:9]
contador_regressivo_1 = 10
soma_primeiro_digito = 0

print('função  para o primeiro digito')
for digito in nove_digitos:
    digito = int(digito)
    soma_primeiro_digito += digito * contador_regressivo_1
    contador_regressivo_1 -= 1
    print(f'{digito} x {contador_regressivo_1} = {digito * contador_regressivo_1}  ', end=' ')

primeiro_digito = (soma_primeiro_digito * 10) % 11
print(f'\n{primeiro_digito}')
primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito
print(f'Primeiro digito é {primeiro_digito}')
#calculo do segundo digito
dez_digitos =  nove_digitos + str(primeiro_digito)
contador_regressivo_2 = 11
soma_segundo_digito = 0

print('\nFunção do segundo digito')
for digito in dez_digitos:
    digito = int(digito)
    soma_segundo_digito += digito * contador_regressivo_2
    contador_regressivo_2 -= 1
    print(f'{digito} x {contador_regressivo_2} = {digito * contador_regressivo_2}  ', end=' ')

segundo_digito = (soma_segundo_digito * 10) % 11
print(f'\n{segundo_digito}')
segundo_digito = 0 if segundo_digito > 9 else segundo_digito
print(f'Segundo digito é {segundo_digito}')

novo_cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
if cpf_enviado_usuario == novo_cpf_gerado:
    print(f'Novo CPF gerado {novo_cpf_gerado} é válido.')
else:
    print('CPF inválido.')