


def bfs(grafo, graforesidual, source, target, pai):
  vertices = len(grafo)
  visitados = [0]*vertices
  fila = []
  fila.append(source)
  visitados[source] = 1
  pai[source] = -1
  while(fila):
    u = fila.pop(0)
    for v in grafo[u]:
      if(not visitados[v] and graforesidual[u][v] > 0):
        fila.append(v)
        pai[v] = u
        visitados[v] = 1
  return(visitados[target])


def ford(grafo, matrizgrafo, source, target):
  vertices = len(grafo)
  graforesidual = list(map(list, matrizgrafo))
  pai = [0]*vertices
  fluxo = 0
  while(bfs(grafo, graforesidual, source, target, pai)):
    fluxocaminho = 2**33
    v = target
    caminho = []
    while(v!= source):
      caminho += [v]
      u = pai[v]
      fluxocaminho = min(fluxocaminho, graforesidual[u][v])
      v = pai[v]
    caminho += [v]
    v = target
    while(v != source):
      u = pai[v]
      graforesidual[u][v] -= fluxocaminho
      graforesidual[v][u] += fluxocaminho
      v = pai[v]
    fluxo += fluxocaminho
  return fluxo


N, M = map(int, input().split(' '))

grafo = [[] for i in range (N)]
matrizgrafo = [[0]* N for i in range (N)]

for i in range(M):
  u, v = map(int, input().split(' '))
  grafo[u] += [v]
  grafo[v] += [u]
  if(matrizgrafo[u][v] == 0):
    matrizgrafo[u][v] = 1
  else:
    matrizgrafo[u][v] += 1

print(ford(grafo, matrizgrafo, 0, N-1))
