from datetime import date
atual = date.today().year
nas = int(input('Qual o ano de nascimento do atleta\n '))
idade = atual - nas
print('o atleta tem {}'.format(idade))

print('com idade {} e  e hoje é {} '.format(idade,atual))
if idade<= 9:
    print('vc esta na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('vc esta na categoria INFANTIL'.format((idade)))
elif idade<= 19:
    print('vc esta na categoria,JUNIOR NENEM QUE SORTE'.format(idade))
elif idade<= 25:
    print('vc esta na categoria,SÊNIO VOVÔ'.format(idade))
elif idade> 25:
    print('vc esta na categoria,mastER QUE SORTE'.format(idade))

