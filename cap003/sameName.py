from pkg_resources import EGG_DIST


def spam():
    global eggs
    eggs = 'spam'
    print(f'Dentro de spam - como: {eggs}')

print()
print('-=-' * 5)
eggs = 'global'
print(f'Fora de spam -  como: {eggs}')
spam()
print(eggs)

print()
print('-*-' * 5)