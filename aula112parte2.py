# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
#Decoraçoes são "Syntax Sugar" (Açúcar sintatico)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)

        resultado = func(*args, **kwargs)
        resultado += ' QUAKL'
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorado')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError ('param deve ser uma string')



# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
invertida = inverte_string('123')
print(invertida )