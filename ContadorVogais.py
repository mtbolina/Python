print("Contador de vogais !" )

string=input("Digite uma string: ") #aloca a entrada do usuario em uma variavel

vogais="AEIOUaeiou"  #identificacao das vogais

contador = 0 

for letras in string:       #laco de repeticao que percorre a entrada do usuario e
    if letras in vogais:     #>> verifica quantas vogais existe na entrada
        contador +=1        #conta o numero de vogais

print(f"O numero de vogais dentro da string  '{string}'  e {contador}")  #imprime o resultado
