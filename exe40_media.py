print("""
==============================
      digite suas notas no formato x.x
==================================""")
n1 = float(input('qual a sua primeira nota ?  '))
n2= float(input('qual a sua seguna nota?  '))

m = (n1+n2)/2
print('com suas notas {:.2f} e {:.2f} a medica ficou em {:.2f}'.format(n1,n2,m))
if m<5:
    print('vc esta reprovado manoooo sua media foi baixa em {:.2f}'.format(m))
elif 5 < m < 6.9:
    print('vc ficou em recuperação media {:.2f}'.format((m)))
elif m>7.0:
    print('vc passou direto maluco e com média {:.2f}, QUE SORTE'.format(m))

