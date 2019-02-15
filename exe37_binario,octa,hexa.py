num = int(input('digite um numero:'))
print('''Escolha uma das opções abaixo para conversão: '
      [1] BINARIO
      [2] OCTAL
      [3] HEXADECIMAL''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('{} em binario é igal a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} em octal é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} em hexadecinal é igual a {}'.format(num,hex(num)[2:]))

else:
    print('tente outra ooção, nova tentativa')
