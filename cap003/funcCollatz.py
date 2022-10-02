# Se number for par, collatz() deverá exibir number // 2 e retornar esse valor. Se number for ímpar, collatz() deverá exibir e retornar 3 * number + 1.

def collatz(number):
    numberValid = False
    # Este bloco try verifica se o número pode ser convertido para inteiro
    try:
        n = int(number)
        numberValid = True
    # Se não for possível a conversão vai solicitar outro número    
    except:
        print('Digite um número inteiro válido.')
        res = number
    
    if numberValid:

        # Aqui testa se o número é um par
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




    