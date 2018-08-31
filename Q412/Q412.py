tamanho = int(input())
quantidadeamigos = int(input())

proximidade = []

for i in range (0, quantidadeamigos):
  x = input().split()
  x[0] = int(x[0])
  x[1] = float(x[1])
  proximidade.append(x)

proximidade = sorted(proximidade, key = lambda x: (x[0]))

atualizacoes = int(input())
fim = []
tempo = []
for i in range (0, atualizacoes):
  x = input().split(' ')
  x[0] = int(x[0])
  x[1] = float(x[1])
  frase = x[2:]
  string = ' '.join(frase)
  y = 0.8*proximidade[x[0]-1][1] + 0.2*x[1]
  fim.append([proximidade[x[0]-1][0], y, string])


fim = sorted(fim, key=lambda x: (x[1]), reverse = True)

for i in range (0, tamanho):
  print(fim[i][0] ,fim[i][2])

