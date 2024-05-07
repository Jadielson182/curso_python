
palavra_secreta = 'dinheiro'
palavra_completa = ''
contador = 0



while True:

    letra = input('\nDigite uma letra: ')

    contador += 1

    if len(letra) > 1:

        print('Digite apenas uma letra.')

        continue

    if letra not in palavra_secreta:

        print('Letra não encontrada na palavra sectreta')

        continue

    if letra in palavra_secreta:
        palavra_completa += letra

    palavra_formada = ''
    for  letra_secreta in palavra_secreta:

        if letra_secreta in palavra_completa:

            palavra_formada += letra_secreta

        else:

            palavra_formada += '*'        
    
    print('palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Parabens! Voçê ganhou!'

        f'A palavra era : {palavra_secreta}'

        f'Foram {contador} tentativas.'
        )
        palavra_completa = ''
        contador = 0



