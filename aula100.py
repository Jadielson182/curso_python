# Generator expression, Irerables e iterators em python

# iterable = ['Eu', 'ttenho', '__iter__']
# iterator = iter(iterable) # tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

import sys

iterable = ['Eu', 'ttenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


print(generator)


for n in generator:
    print(n)
