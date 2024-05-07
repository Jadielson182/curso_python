def duplicar(dobro):  
    valor = dobro * 2
    return valor


def triplicar(triplo):
        valor = triplo * 3
        return valor


def quadruplicar(quadruplo):
    valor = quadruplo * 4
    return valor



numero = int(input('Digite um número: '))
print(f'O dobro de {numero} é ', duplicar(numero))
print(f'O triplo de {numero} é ', triplicar(numero))
print(f'O quadruplo de {numero} é ', quadruplicar(numero))