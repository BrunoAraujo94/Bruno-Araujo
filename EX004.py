#Faça um programa que leia algo pelo teclado e mostre na tela o seu
#tipo primitivo e todas as inormações possiveis sobre ela
#Exercício OO4 resolvido em Python 3.0
a = input('Digite algo')
print("só tem espaços ? ",a.isspace())
print('É um numero ? ',a.isnumeric())
print('È alfabético ? ',a.isalpha())
print('É alphanumérico ?',a.isalnum())
print('Esta em Maíscula ?',a.isupper())
print('Esta em minúscula ?',a.islower())
print('Esta Capitalizada?',a.istitle())

