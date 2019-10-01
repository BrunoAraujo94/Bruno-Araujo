#FAÇA UM PROGRAMA QUE LEIA U NUMERO INTEIRO QUALQUER
#E MOSTRE NA TELA SUA TABUADA
valor = int(input('Entre com um numero para saber a tabuada : '))
aux = 0
print('*'*18)
print('Tabuada de {}'.format(valor))
print('*'*18)
while(aux<=10):
    print('{0} X {1}= {2}'.format(aux, valor, (aux*valor)))
    aux = aux + 1
print('*'*18)
print('{} x {:2} = {} '.format(valor, 1, valor*1))
print('{} x {:2} = {} '.format(valor, 2, valor*2))
print('{} x {:2} = {} '.format(valor, 3, valor*3))
print('{} x {:2} = {} '.format(valor, 4, valor*4))
print('{} x {:2} = {} '.format(valor, 5, valor*5))
print('{} x {:2} = {} '.format(valor, 6, valor*6))
print('{} x {:2} = {} '.format(valor, 7, valor*7))
print('{} x {:2} = {} '.format(valor, 8, valor*8))
print('{} x {:2} = {} '.format(valor, 9, valor*9))
print('{} x {:2} = {} '.format(valor, 10, valor*10))
print('*'*18)