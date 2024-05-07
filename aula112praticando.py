
def criar_funcao(funcao):
    def interna(*args,**kwargs):
        print('Começando a decoração')
        for arg in args:
            is_string(arg)
        resultado = funcao(*args, **kwargs)
        resultado += ' pronto'
        print(f'A resposta é {resultado}')
        print('Você passou pela decoração')
        return resultado
    return interna
    
        



def is_string(param):
    if not isinstance(param,str):
        raise TypeError ('Parâmetro não é string')



@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]



invertida = inverte_string('123')
# checando_string = criar_funcao(inverte_string)
# invertida = checando_string('123')
print(invertida)