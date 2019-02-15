from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} e tem {} ANOS EM {}'.format(nasc, idade, atual))

if idade == 18:
    print('Voce deve se alistar mano!')
elif idade < 18:
    saldo = 18 - idade
    print('aguarde pois nao tem faltam {} anos'.format(saldo))

elif idade > 18:
    saldo = idade - 18
    print("parabens se alistou a {} anos ".format(saldo))

