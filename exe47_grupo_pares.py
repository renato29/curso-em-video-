soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 ==0:

        soma = soma + c
        cont = cont +1
print('a soma de todos os nmeros é {}\n e a contagem deu {}'.format(soma,cont))
