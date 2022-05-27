idade = int(input('Digite sua idade: '))
if idade < 16:
    print('Menor de idade, não vota')
elif idade < 18:
    print('Adolescente, voto opcional')
elif idade < 65:
    print('Adulto, voto obrigatório')
else:
    print('Idoso, voto opcional')