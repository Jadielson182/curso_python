def criar_multplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar



duplicar = criar_multplicador(2)
triplicar = criar_multplicador(3)
quadruplicar = criar_multplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))