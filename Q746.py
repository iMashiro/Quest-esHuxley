def matriz(linhas, colunas):
  matriz = []
  n = linhas
  for i in range(n):
    tmp = []
    x = input()
    x = x.split(" ")
    for j in range(colunas):
        elemento = int(x[j])
        tmp.append(elemento)

    matriz.append(tmp[:])  
  return matriz
    
def prodMatrix(matrizA, matrizB):

    sizeLA = len(matrizA)
    sizeCA = len(matrizA[0])
    sizeCB = len(matrizB[0])
    matrizR = []
    for i in range(sizeLA):
        matrizR.append([])
        for j in range(sizeCB):
            val = 0
            for k in range(sizeCA):
                    val += matrizA[i][k]*matrizB[k][j]
            matrizR[i].append(val)
    return matrizR

     

x = input()
N, M, O = x.split(" ")
N = int(N)
M = int(M)
O = int(O)
M1 = matriz(N, M)
M2 = matriz(M, O)

M3 = prodMatrix(M1,M2)

for i in range (0, O):
  for j in range (0, N):
    if(j == N - 1):
      print(M3[i][j], end="")
    else:
      print(M3[i][j], end=" ")
  print()

        
