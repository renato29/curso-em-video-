casa = float(input('Qual o valor do bem desejado: R$'))
sal = float(input('Qual o salário do cliente '))
mora = float(input('Quantos anos de pagamento ? '))
prestação = casa/(mora*12)
min = sal* 30/100
print('a da casa  será de R${:.2f} pagando em {}'.format(casa, mora))
print('a prestação será de R${:.2f}'.format(prestação))
if prestação<=min:
    print('emprestimo aprovado')
else:
    print('emprestimo impossivel hoje, retorno em um ano')
