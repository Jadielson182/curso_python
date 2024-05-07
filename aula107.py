import importlib

import aula107_m

print(aula107_m.variavel)

for i in range(10):
    importlib.reload(aula107_m)
    print(i)

print('FIM')