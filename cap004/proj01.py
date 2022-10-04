cont = True

while cont:
    res = list(input('Digite uma lista ou nada para sair: '))
    if not res:
        print('Saindo....')
        break
    else:
        for i in range(len(res)):
            if i == (len(res) - 2):
                print(f'{res[i]}, and ', end='')
            elif i == (len(res) - 1):
                print(f'{res[i]}')
            else:
                print(f'{res[i]}, ', end='')
