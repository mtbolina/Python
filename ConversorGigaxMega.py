def Mega(valor):
    return valor*1024

giga=float(input("Digite o tamanho do arquivo em Gigabytes: "))

ConversorMega=Mega(giga)

print(f"O arquivo de {giga} Gigabytes tem o tamanho de {ConversorMega} Megabytes.")
