
def teste(vetor2, x):
  soma = 0
  for k in range(len(vetor2)):
    if(vetor2[k] >= (x)):
      soma += (vetor2[k] - (x))
  return soma


def busca(vetor2, esquerda, direita, soma):
  meio = int((esquerda + direita) / 2)
  x = teste(vetor2, meio)
  if(esquerda == direita):
    return 0
  if(soma == x):
    for i in range (len(vetor2)):
      maisproxima = meio
      if(meio == vetor2[i]):
        return(meio)
      elif(vetor2[i] < meio):
        if(meio - vetor2[i] > maisproxima and meio > vetor2[i]):
          maisproxima = meio - vetor2[i]
    return(meio-maisproxima)
  elif(soma > x):
    return busca(vetor2, esquerda, meio, soma)
  else:
    return busca(vetor2, meio+1, direita, soma)


vetor = input()
vetor = vetor.split()
vetor = list(map(int,vetor))

vetor2 = input()
vetor2 = vetor2.split()
vetor2 = list(map(int,vetor2))
vetor2 = sorted(vetor2)

maior = 0
menor = vetor2[0]
for i in range(len(vetor2)):
  if(vetor2[i] > maior):
    maior = vetor2[i]
  if(vetor2[i] < menor):
    menor = vetor2[i]
soma = 0
while soma == 0:
  soma = busca(vetor2, menor, maior, vetor[1])
  if(soma == 0):
    vetor[1] += 1 
    soma = 0
print(soma)   
  
  
