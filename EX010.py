#CRIE UM PROGRAMA QUE LEIA A QUANTIDADE DE DINHEIRO QUE A
#PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE
#COMPRAR
real = float(input("Informe a quantidade de reais para conversão: BRL "))
cotacao = float(input('Informe a cotação do Dolar : '))
conversao = real/cotacao
print('A quantidade de dólar convertido em real é: R$',conversao)