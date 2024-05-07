lista_de_produtos = []
while True:
    print('Selecione uma opção.')
    escolha = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    if len(escolha) > 1:
        continue
    elif escolha == 'i':
        produto = input('O que sera cadastrado? ')
        lista_de_produtos.append(produto)
    elif escolha == 'l':
            for indice, nome in enumerate(lista_de_produtos):
                print(indice, nome)
            if lista_de_produtos == []:
                print('nada para listar')
    elif escolha == 'a':
        apagar = input('Escolha o índice para apagar: ')
        try:
            apagar = int(apagar)
            lista_de_produtos.pop(apagar)
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif escolha == 's':
        break
    else:
        print('Por favor escolha i, a, l ou s.')
        continue
print('Fim  do programa.')