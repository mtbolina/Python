def Mega(valor):
    return valor*1024

def Kilo(valor):
    return valor*1024*1024

giga=float(input("Digite o tamanho do arquivo em Gigabytes: "))

ConversorMega=Mega(giga)
ConversorKilo=Kilo(giga)

print(f"O arquivo de {giga} Gigabytes tem o tamanho de {ConversorMega} Megabytes.")
print(f"O arquivo de {giga} Gigabytes tem o tamanho de {ConversorKilo} Kilobytes.")
