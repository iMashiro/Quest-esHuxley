import sys
sys.setrecursionlimit(1000000)

def maior(x, y):
  if(x > y):
    return x
  else:
    return y

def acharmaior(buscado):
  if(buscado == 0):
    return 0
  if(solucao[buscado] != -1):
    return solucao[buscado]
  melhor = -1
  for i in range (1, buscado + 1):
    x = precos[i-1] + acharmaior(buscado-i)
    if(melhor < x):
      melhor = x
  solucao[buscado] = melhor
  return melhor

casos = int(input())
while casos != 0:
  precos = []
  solucao = [-1] * (casos+1)
  for i in range (casos):
    precos.append(int(input()))
  print(acharmaior(casos))
  casos = int(input())
