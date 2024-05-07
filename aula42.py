frase = 'O python é uma linguagem '\
     'multiparadigma. '\
     'pyton foi criado por Guido van Rossum.'

i = 0

qtd_apareceu_mais_vezes = 0

letra_apareceu_mais_vezes = ''


while i < len(frase):

    letra_atual = frase[i]


    if letra_atual == ' ':

        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '

    f'"{letra_apareceu_mais_vezes}" que apareceu '

    f'{qtd_apareceu_mais_vezes}x')



# frase = 'O python é uma linguagem '\

#     'multiparadigma. '\

#     'pyton foi criado por Guido van Rossum.'


# quando_apareceu = 0
# mais_letras = ''

# i = 0


# while i < len(frase):

#     letra_atual = frase[i]

#     if letra_atual == ' ':

#         i += 1
#         continue

#     quando_apareceu_atual = frase.count(frase[letra_atual])


#     if quando_apareceu < quando_apareceu_atual:
#         quando_apareceu = quando_apareceu_atual
#         mais_letras = letra_atual


#         i += 1
        



