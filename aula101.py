# Introdução às Generator funcions em python
# generator = (n for n in range(100))


# def generator(n=0, maximum=10):
#     yield 1  #pausar
#     print('continuando')
#     yield 2   #pausar
#     print('Mais uma...')
#     yield
#     print('Vou termina')
#     return  'ACABOU'


#     gen = generator(n=0)
#     for n in gen:
#         print(n)


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(n=0) # (n=5, maximum=8)   maximum = 10000
for n in gen:
    print(n)
 