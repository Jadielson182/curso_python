# Exercício  com funções


def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total



resultado = mult(3, 4, 6, 3, 2)
print(resultado)


