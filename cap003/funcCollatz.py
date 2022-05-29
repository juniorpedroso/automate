def collatz(number):
    numberValid = False
    try:
        n = int(number)
        numberValid = True
    except:
        print('Digite um número inteiro válido.')
        res = number
    
    if numberValid:
        if (n % 2) == 0:
            res = n // 2
            print(res)
        else:
            # print(n)
            res = (n * 3) + 1
            print(res)
    if numberValid: 
        return res

print()
n = input('Digite um número: ')

while True:
    n = collatz(n)
    if n == 1:
        break
    elif type(n) != int:
        n = input('Digite um número: ')




    