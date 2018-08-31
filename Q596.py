def buscarcaminho(atual, contador):
  fila = []
  fila.append(atual)
  distancia = {}
  for x in dic:
    distancia[x] = -1
    visitados[x] = "Branco"
  distancia[atual] = 0
  visitados[atual] = "Preto"
  while fila:
    aux = fila.pop(0)
    for i in dic[aux]:
      if(visitados[i] == "Branco"):
        visitados[i] = "Preto"
        distancia[i] = distancia[aux] + 1
        fila.append(i)    
  return distancia

casos = int(input())
for i in range (casos):
  vetor = input()         #VETOR[0] = N�MERO DE ILHAS  /   VETOR[1] = N�MERO DE PONTES
  vetor = vetor.split()
  vetor = list(map(int, vetor))
  dic = {}
  dic[1] = []
  dic[vetor[0]] = []
  visitados = {}
  for j in range (vetor[1]):
    vetor2 = input()
    vetor2 = vetor2.split()
    vetor2 = list(map(int, vetor2))
    if(vetor2[0] not in dic):
      dic[vetor2[0]] = []
      visitados[vetor2[0]] = "Branco"
    dic[vetor2[0]].append(vetor2[1])
    if(vetor2[1] not in dic):
      dic[vetor2[1]] = []
      visitados[vetor2[1]] = "Branco"
    dic[vetor2[1]].append(vetor2[0])
  contador = []
  contador = buscarcaminho(1, contador)
  print(contador[vetor[0]])
