from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''ESCOLHA UMA OPÇÂO 
[0] PEDRA
[1] PAPEL
[2] TESOURRRA
''')

jogador: int = int(input('Qual é a sua jogada???'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 12)
print('o computador escolheu {}'.format(itens[computador]))
print('jogador jogou {}.'.format(itens[jogador]))
print('-=' * 12)
if computador == 0: #jogou pedra
    if jogador ==0:
        print('empate')
    elif jogador ==1:#papel
        print('jogador vence')
    elif jogador ==2:#tesoura
        print('computador vence')
    else:
        print('JOGADA INVALIDA SAFADO!!!')
elif computador ==1: #jogou papel
    if jogador ==0:
       print('computador vence')
    elif jogador ==1:
        print('empate')
    elif jogador ==2:
        print('jogador vence')
    else:
        print('JOGADA INVALIDA SAFADel!!!')
elif computador ==2: #jogou tesoura
    if jogador ==0:
        print('jogador vence')
    elif jogador ==1:
        print('computador vence')
    elif jogador ==2:
        print('empate safadões')
    else:
        print('JOGADA INVALIDA SAFADO!!!')
