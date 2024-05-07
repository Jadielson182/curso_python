"""

Lista de listas e seus índices
"""

salas   = [

       #0    índices    1

    ['Maria', 'Helena',], #  0

     #  1  índides

    ['Elanine',], #  1

    #  1       2         3   índices

    ['Luis', 'João', 'Eduarda',],  # 2
]

# print(salas[1][0])

# print(salas[0][1])
# print(salas[2][2])

# print(salas[2][3][2])


for sala in salas:
    print(f'A sala é {sala}')

    for aluno in sala:
        print(aluno) #;print(sala)