#Decoradores com parametro
def fabrica_de_Decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')
        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


    return fabrica_de_funcoes

@fabrica_de_Decoradores(1, 2, 3)
def soma(x, y):
    return x + y


# @fabrica_de_Decoradores(1, 2, 3)
# def multiplica(x, y):
#     return x * y

# @fabrica_de_Decoradores(1, 2, 3)
# def divisao(x, y):
#     return x - y

decoradora = fabrica_de_Decoradores() 
multiplica = decoradora(lambda x, y: x * y) # ou poderia usar # multiplica = fabrica_de_Decoradores()(lambda x, y: x * y)

# # divisao = fabrica_de_Decoradores(1, 2, 3)(lambda x, y: x - y)

de_mais_cinco = soma(10, 5)

dez_vezes_cinco = multiplica(10, 5)
# # dez_menos_5 = divisao(10, 5)
print(de_mais_cinco)
print(dez_vezes_cinco)

# print(dez_menos_5)

