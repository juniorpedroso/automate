from pkg_resources import EGG_DIST


def spam():
    global eggs
    eggs = 'spam' # Essa é a variável global

def bacon():
    eggs = 'bacon' # Essa é uma variável local

def ham():
    print(eggs) # essa é a variável global

eggs = 42 # essa é a variável global
spam()
print(eggs)

