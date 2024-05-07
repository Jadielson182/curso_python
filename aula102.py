# Try, except, else e finally

# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    print(b[0])
    print('Linha 1')
    c = a / b
    print('pinha 2')

except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except TypeError:
    print('TypeError + IndexError')
except Exception:
    print('ERRO DE SCONHECIDO')

print('CONTINUA')
