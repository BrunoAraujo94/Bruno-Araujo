#CRIE UM ALGORITIMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO
#TRIPLO E A RAIZ QUADRADA
n1 = int(input('Digite um numero : '))
d = n1*2
t = n1*3
r = n1**(1/2)
print('Com a análise do numero {}, o seu dobro é {}, o triplo é {}, \ne sua raiz quadrada é {:.2f}'.format(n1,d,t,r))