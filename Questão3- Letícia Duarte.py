#QUESTAO3


print("Fun��es recursivas s�o fun��es que chamam a si mesma de forma que, para resolver um problema maior, utiliza a recurs�o para chegar as unidades b�sicas do problema em quest�o e ent�o calcular o resultado final.\n Exemplo:")

def fatorial(n):

  if (n==1):

    return (n)

  return fatorial(n-1)*n-1

print(fatorial(5))
