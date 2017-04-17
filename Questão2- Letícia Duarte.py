#QUESTAO2

import random

sorteados = []

alunos={}

nome= str(input("entre com seu nome:"))

matricula=str(input("entre com sua matricula:"))

def adicionarSorteado(sorteados):

  sorteio= random.randint(1,100)

  sorteados.append(sorteio)

  print(sorteados)

def adicionarAluno(alunos,matricula,nome):

  
 alunos[matricula]=nome

def exibirAlunos(alunos):

  print(alunos)

def buscarAluno(alunos, matricula):

  matricula= str(input("entre com sua matricula:"))

  print (alunos[matricula])

adicionarSorteado(sorteados)

adicionarAluno(alunos,matricula,nome)

exibirAlunos(alunos)

buscarAluno(alunos, matricula)