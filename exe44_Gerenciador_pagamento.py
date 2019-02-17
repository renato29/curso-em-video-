print('-=' * 20)
print('{:^40}'.format('Lojas MERINO'))
print('-=' * 20)
preço = float(input('Preço final das compras: R$'))
print('''FORMAS DE PAGAMENTO 
[1] À VISTA DINHEIRO
[2] À VISTA NO DEBITO
[3] CREDITO 2X
[4] CREDITO 3X OU MAIS ''')
opção = int(input('Qual é a opção desejada pelo cliente?\n'))
if opção==1:
    total = preço - (preço*10/100)
elif opção==2:
    total = preço - (preço *5/100)
elif opção==3:
    total = preço
    parcela= total/2
    print('sua compra parcelada em 2 vezes será de {:.2f}'.format(parcela))
elif opção==4:
    total = preço + (preço *20/100)
    totpar = int(input('Quantas parcelas pra esse muquirana??'))
    parcela=total/totpar
    print('A sua compra será parcelada em {}x  de R$ {:.2f}'.format(totpar,parcela))
print('A sua comprar de R$ {:.2f} vai custar R${:.2f}'.format(preço,total))

