


# https://stackoverflow.com/questions/2386714/why-is-import-bad



# from sys import path


# import aula108_package.modulo


# from aula108_package.modulo import soma_do_modulo


# from aula108_package import modulo


# from aula108_package.modulo import *  # ma pratica



# # print(*path, sep='\n')
# # print(__name__)



# print(soma_do_modulo(1, 2))


# print(aula108_package.modulo.soma_do_modulo(1, 2))


# print(modulo.soma_do_modulo(1, 2))


# print(variavel)


# print(nova_variavel)



# from aula108_package.modulo import soma_do_modulo, fala_oi
# print(__name__)
# fala_oi()



from aula108_package import soma_do_modulo, fala_oi



print(soma_do_modulo(2, 1))
fala_oi()