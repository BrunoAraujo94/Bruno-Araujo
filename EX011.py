#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE
#EM METROS E CALCULE A SUA AREA E A QUANTIDADE
#DE TINTA NECESSÁRIA PARA PINTALA, SABENDO QUE CADA LITRO
#DE TINTA PINTA UMA AREA DE 2M2
L = int(input("Digite a largura da área : "))
C = int(input('Digite o comprimento da área : '))
A = L*C
Litros = A/2
print('A área total é {}'.format(A))
print('Será necessário um total de {} litros de tita para pintar toda a área'.format(Litros))