valorHora=float(input("Digite o valor ganho por hora: "))
horasTrabalhadas=float(input("Digite a quantidade de horas trabalhadas: "))

SalarioBruto=valorHora*horasTrabalhadas
ImpostoDeRenda=SalarioBruto*0.11
INSS=SalarioBruto*0.08
Sindicato=SalarioBruto*0.05
descontos=ImpostoDeRenda+INSS+Sindicato
Salarioliquido=SalarioBruto-descontos


print(f" Salario Bruto: R${SalarioBruto}")
print(f" IR (11%): R${ImpostoDeRenda}")
print(f" INSS (8%): R${INSS}")
print(f" Sindicato (5%): R${Sindicato}")
print(f" Salario Liquido: R${Salarioliquido}")             

