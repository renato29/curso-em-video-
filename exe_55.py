from builtins import print

maior = 0
menor = 0
for p in range(1 ,6):
    peso = float(input('Peso {}ª pessoa.'.format(p)))
    if p == 1 :
        maior= peso
        menor= peso
    else:
        if peso> maior:
            maior = peso
        if\
            peso< menor:
            menor = peso

print( ' maior peso lido foi de {}Kg'.format (maior))
print('o menor peso lido foi de {}kg'.format (menor))