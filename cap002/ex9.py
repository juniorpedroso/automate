from random import randint

while True:
    print()
    spam = int(input('Digite um número de 1 a 3 ou (q) para sair: '))
    if spam == 'q':
        print('Ok. Goodbye!!')
        break
    elif spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    elif spam == 3:
        print('Greetings!')
        