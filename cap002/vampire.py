name = input('Digite seu nome: ')
age = int(input('Qual é sua idade?: '))
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not a undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
