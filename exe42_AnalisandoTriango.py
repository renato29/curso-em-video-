"""
EXERCÍCIO 035: Analisando Triângulo v2.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo !')
    if r1==r2==r3:
        print("equilatero ! ! ! ")
    if r1!=r2!=r3:
        print('ele faz um triangulo escaleno')
    else:
        print('O triangulo é isóceles ! ')
else:
    print('os seguimentos acima nao formam um traingulo')
#if dentro de if é uma condição alinhada #
