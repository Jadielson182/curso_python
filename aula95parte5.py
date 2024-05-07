# List comprehension em python: tudo o que voçê precisa saber parte 5

nomes = ['Luiz', 'Maria', 'Helena', 'Joana', 'Felipe' ]
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}' 
    for nome in nomes]
print(novos_nomes)