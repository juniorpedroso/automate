from tkinter import N


def collatz(number):
    numberValid = False
    try:
        n = int(number)
        numberValid = True
    except:
        print('Digite um número inteiro válido.')
    
    print(f'Você digitou {number}')
    if numberValid:
        if n % 2 == 0:
            res = n // 2
            print(res)
        else:
            print(n)
            res = (n * 3) + 1


print()
n = input('Digite um número: ')
collatz(n)




    