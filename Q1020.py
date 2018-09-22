import heapq

def acharmenor():
  custototal = 0
  distancias[0] = 0
  vetor = []

  fila = [(0, 0, 0)]

  while len(vetor) < V:
    atual = heapq.heappop(fila)
    if(atual[1] not in vetor):
      custototal += atual[0]
      vetor.append(atual[1])
      distancias[atual[1]] = distancias[atual[2]] + atual[0]
      if(atual[1] < atual[2]):
        conexoes[atual[1]].append(atual[2])
        conexoes[atual[1]].sort()
      elif(atual[1] > atual[2]):
        conexoes[atual[2]].append(atual[1])
        conexoes[atual[2]].sort()
      for aux in grafo[atual[1]]:
        heapq.heappush(fila, (aux[0], aux[1], atual[1]))
  return custototal, distancias, conexoes


V, E, R = map(int, input().split(' ')) 
#V = quantidade de nós na rede 
#E = quantidade de possíveis interligações
#R = velocidade da rede
grafo = {}
distancias = {}
conexoes = {}
for i in range (V):
  distancias[i] = 999999999
  grafo[i] = []
  conexoes[i] = []
for i in range (E):
  A, B, C = map(int, input().split(' '))
  grafo[A].append((C, B))
  grafo[B].append((C, A))

custo, distancias, conexoes = acharmenor()
print("########################\n" + "Minimum Cost:\n" + str(custo))
print("########################\n" + "Connections:")
for i in conexoes:
    for j in conexoes[i]:
        print(i,j)
print("########################\n" + "Pings:")
for i in range(1, V):
    print(str(i) + ": " + "%.3f" % ((distancias[i] * 2) / R))
print("########################")

