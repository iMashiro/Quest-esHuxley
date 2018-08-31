import sys
sys.setrecursionlimit(1000000)
def calculardistancia(x, distanciatotal):
  visitados[x[0]] = "Preto"
  for i in cidades[x[0]]:
    if visitados[i[0]] == "Branco":
      distanciatotal = calculardistancia(i, distanciatotal)
      imposto[x[0]] += imposto[i[0]]
      imposto[i[0]] = 0
  if imposto[x[0]] % parametros[1] == 0:
      distanciatotal += 2 * x[1] * (int(imposto[x[0]] / parametros[1]))
  else:
      distanciatotal += 2 * x[1] * (int(imposto[x[0]] / parametros[1]) + 1)
  return(distanciatotal)
#------------------------------------------------------------------------------------------

parametros = input()
parametros = parametros.split()
parametros = list(map(int, parametros))

#Parametros[0] = Quantidade de cidades -> N
#Parametros[1] = Carga m�xima da carruagem -> C

imposto = {}
i = 1
for k in input().split(' '):
    imposto[i] = int(k)
    i += 1

#Imposto cont�m o valor dos impostos de cada cidade -> Ei

cidades = {}
visitados = {}
for k in range (parametros[0] - 1):
  vetor = input()
  vetor = vetor.split()
  vetor = list(map(int, vetor))
  if vetor[0] not in cidades:
    cidades[vetor[0]] = []
    visitados[vetor[0]] = "Branco"
  cidades[vetor[0]].append((vetor[1], vetor[2]))
  if vetor[1] not in cidades:
    cidades[vetor[1]] = []
    visitados[vetor[1]] = "Branco"
  cidades[vetor[1]].append((vetor[0], vetor[2]))

distanciatotal = 0
distanciatotal = calculardistancia((1,0), distanciatotal)
print(distanciatotal)

#------------------------------------------------------------------------------------------



