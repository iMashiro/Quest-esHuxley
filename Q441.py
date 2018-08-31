#BFS ------------------------------------------------------------
def BFS(par, i):
  fila = []
  fila.append(par)
  visited[par] = i
  while fila:
    aux = fila.pop(0)
    for x in pares:
      if (visited[x] == 0):
        if(x[0] == aux[0] or x[0] == aux[0]+1 or x[0] == aux[0]-1):
          if(x[1] == aux[1] or x[1] == aux[1]+1 or x[1] == aux[1]-1):
            fila.append(x)
            visited[x] = i
#FIM DA BFS -----------------------------------------------------

#FLOOD FILL -----------------------------------------------------
def floodfill(pares, visited):
  contador = 0
  for posicao in pares:
    if(visited[posicao] == 0):
      contador += 1
      BFS(posicao, contador)
  return contador
#FIM DO FLOOD FILL -----------------------------------------------

#MAIN ------------------------------------------------------------
contadorcasos = 0
while True:
  try:
    contadorcasos += 1
    #LEITURA DO TAMANHO E DA MATRIZ ------------------------------
    size = int(input())
    lista = []
    for i in range (size):
      aux = input()
      aux2 = []
      for j in range (size):
        aux2.append(aux[j])
      lista.append(aux2)
    #FIM DA LEITURA DA MATRIZ ------------------------------------
    pares = []
    #COMECO DO FLOOD FILL ----------------------------------------
    visited = {}
    for i in range (size):
      for j in range (size):
        if (lista[i][j] == '1'):
          base = (i, j)
          pares.append(base)
          visited[base] = 0
    #FIM DO FLOOD FILL -------------------------------------------
    
    numerobases = floodfill(pares, visited)
    
    print("Image number " + str(contadorcasos) + " contains " + str(numerobases) + " war eagles.")

  except EOFError:
    break
