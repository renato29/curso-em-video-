somaidade  = 0
mediaidade = 0
nomevelho = 0
maioridadedehomem = 0
idade = 0
totmulher20=0
for p in range (1,5):
    print('-----{}a Pessoa ------'.format (p))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    somaidade += idade
    if p== 1 and sexo in "Mm":
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade< 20:
        totmulher20 +=1

mediaidade = somaidade/4
print('a media de idade do grupo é de {} anos'.format(mediaidade))
print("o homem mais velho tem {} anos e se chama {}".format(maioridadedehomem, nomevelho))
print( " Ao todo são {} mulheres com menos de 20 anos0".format(totmulher20))

