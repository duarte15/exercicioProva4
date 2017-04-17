#QUESTAO3


print("Funções recursivas são funções que chamam a si mesma de forma que, para resolver um problema maior, utiliza a recursão para chegar as unidades básicas do problema em questão e então calcular o resultado final.\n Exemplo:")

def fatorial(n):

  if (n==1):

    return (n)

  return fatorial(n-1)*n-1

print(fatorial(5))
