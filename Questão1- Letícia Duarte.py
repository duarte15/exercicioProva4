#questao1


import random

numeros= [1,2,3,4,5]

alunos={"123":"joao", "456":"maria", "789":"jose"}

mensagemProva4=""
print ("Seja bem vindo(a) ao Programa da Prova 4\n")

print ("Uma lista, em Python, � uma sequ�ncia ou cole��o ordenada de valores. Cada valor na lista � identificado por um �ndice.\n")

print("Dicion�rios s�o similiares a outros tipos compostos exceto por eles poderem usar qualquer tipo imut�vel de dados como indice.\n")

print("Estou pronto para manipular listas e dicion�rios na prova!\n")

sorteados=[]

contagem=0

while (contagem<20):

  sorteio= random.randint(1,100)

  sorteados.append(sorteio)

  print("O valor da linha" , sorteio , "�" , contagem)

  contagem+=1

mensagemProva4 = "Prova sobre manipula��o de listas e dicion�rios"

letras= len(mensagemProva4)

print(letras)

mensagemProva4+=". Prova de n�mero 4."