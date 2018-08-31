def matriz(linhas, colunas):
  matriz = []
  x = []
  n = linhas
  for i in range(n):
    tmp = []
    x = input()
    x = list(x)
    for j in range(colunas):
        elemento = x[j]
        tmp.append(elemento)
    matriz.append(tmp[:])  
  return matriz



size = int(input())
tabuleiro = matriz(size, size)

soma = 0
maior = 0
j = 0
for i in range (0, size):
  if(j < 0):
    j = 0
  if(j == 0):
    while j < size:
      if(tabuleiro[i][j] == 'o'):
        soma += 1
      elif(tabuleiro[i][j] == 'A'):
        if(soma > maior):
          maior = soma
          soma = 0
        else:
          soma = 0
      j += 1
  elif (j == size):
    j -= 1
    while j >= 0:
      if(tabuleiro[i][j] == 'o'):
        soma += 1
      elif(tabuleiro[i][j] == 'A'):
        if(soma > maior):
          maior = soma
          soma = 0
        else:
          soma = 0
      j-=1
  if(soma > maior):
    maior = soma
print(maior)