'''hora =input('Digite a hora: ')
hora = int(hora)
if hora == 0 or hora <= 11:
    print('Bom dia')
elif hora == 12 or hora <= 17:
    print('Boa tarde')
elif hora == 18 or hora <= 23:
    print('Boa Noite')
else:
    print(f'{hora} não corresponde a um horario.')'''

hora =input('Digite a hora: ')
try:
    hora = int(hora)
    if hora == 0 or hora <= 11:
        print('Bom dia')
    elif hora == 12 or hora <= 17:
        print('Boa tarde')
    elif hora == 18 or hora <= 23:
        print('Boa Noite')
    else:
        print(f'{hora} não corrsponde a um horario.')
except:
    print('Digite apenas números inteiros')