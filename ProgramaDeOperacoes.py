prog=int(input("Programa de Operações! \n Digite 1-Para iniciar "))

while prog == 1: # laço de repetição que se inicia ao usuário digitar o número 1

 op = int(input("\n Digite: \n 1-Soma \n 2-Subtracao \n 3-Multiplicacao \n 4-Divisao \n"))

 match op:
    case 1 :
        print("Soma!")
        n1=int(input("Digite um numero inteiro: "))
        n2=int(input("Digite outro numero inteiro: "))
        soma= n1+n2
        print("A soma dos numeros e : ",soma)
    case 2 :   
           print("Subtracao!")
           a=int(input("Digite um numero inteiro: "))
           b=int(input("Digite outro numero inteiro: "))
           sub = a-b
           print("A subtracao dos numeros e : ",sub)
    case 3 :
          print("Multiplicacao!")
          x=int(input("Digite um numero inteiro: "))
          y=int(input("Digite outro numero inteiro: "))
          mult = x*y
          print("O resultado da multiplicacao e : ",mult)
    case 4:
          print("Divisao!")
          c=int(input("Digite um numero inteiro: "))
          d=int(input("Digite outro numero inteiro: "))
          div=c/d
          print("O resultado da divisao e : ",div)   

 prog=int(input("\n Deseja continuar? \n Digite: \n 1-Para Continuar \n 2-Para Sair \n"))  # Faz com que o usuário possa interromper ou continuar o laço de repetição

print("Fim do Programa.")  

