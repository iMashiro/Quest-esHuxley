def busca(vetor, chute, esquerda, direita, aux):
  meio = int((esquerda + direita)/2)
  if(esquerda == direita):
    if(vetor[meio] == chute):
      return meio
    return -1
  if(chute > vetor[meio]):
    aux = busca(vetor, chute, meio+1, direita, aux)
  else:
    aux = busca(vetor, chute, esquerda, meio, aux)
  return aux


casos = input().split()
casos = list(map(int,casos))
contador = 1
while(casos[0] != 0 and casos[1] != 0):
  print("CASE#", contador, end= ':\n')
  entrada = []
  chute = []
  for i in range (casos[0]):
    entrada.append(int(input()))
  for i in range (casos[1]):
    chute.append(int(input()))
  aux = -1
  entrada.sort()
  for i in range (len(chute)):
    aux = busca(entrada, chute[i], 0, len(entrada)-1, aux)
    if(aux == -1):
      print(chute[i], "not found")
    else:
      print(chute[i], "found at", aux+1)
  casos = input().split()
  casos = list(map(int,casos))
  contador += 1
