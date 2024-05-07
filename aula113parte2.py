#Decoradores com parametro
def parametro_decorador(nome):
    def decorador(func):
        print('decorador', nome)
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador
    return fabrica_de_funcoes

@parametro_decorador(nome='5')   
@parametro_decorador(nome='4')
@parametro_decorador(nome='3')
@parametro_decorador(nome='2')
@parametro_decorador(nome='1')
def soma(x, y):
    return x + y

# decoradora = parametro_decorador() 
#multiplica = decoradora(lambda x, y: x * y) # ou poderia usar # multiplica = fabrica_de_Decoradores()(lambda x, y: x * y)

de_mais_cinco = soma(10, 5)
# dez_vezes_cinco = multiplica(10, 5)

print(de_mais_cinco)
# print(dez_vezes_cinco)

