import math

altura=float(input("Digite a altura: "))
largura=float(input("Digite a largura: "))

area=altura*largura  #calculo da area da parede

QuantidadeTinta=area/3       # A cobertura da tinta e de 3 metros quadrados por litro de tinta, logo a divisao ocorre com o tamanho da area dividido pelo tamanho da cobertura
QuantidadeLatas=math.ceil(QuantidadeTinta/18)  # O metodo math.ceil arredonda o valor para cima, dividimos por 18, por ser a quantidade de litros em uma lata
PrecoTotal=QuantidadeLatas*80    #multiplicamos por 80 por ser o preco de cada lata

print(f"A area da parede e {area} metros quadrados, a quantidade de latas de tinta usada sera de {round(QuantidadeLatas)} e o preco total sera de R${round(PrecoTotal, 2)}")
