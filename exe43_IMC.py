peso=float(input('Qual é o seu peso?\n Kg='))
altura=float(input('Qual a sua altura?\n m='))

imc = peso/(altura**2)
print('O seu IMC é de: {:.2f}'.format(imc))
if imc<18.5:
    print('O seu imc é abaixo do peso')
elif 18.5 <= imc < 25:
    print('O seu imc é peso ideal')
elif 25 <= imc < 30:
    print('O seu imc é sobrepeso')
elif 30<= imc < 40:
    print('O seu imc é obesidade')
else :
    print('O seu IMC é obesidade morbida =(')
