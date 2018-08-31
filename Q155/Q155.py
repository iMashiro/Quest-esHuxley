def testar(vetor, valor):
  contador = 0
  for i in range (0, len(vetor)):
    contador += int(vetor[i]/valor)
  return contador


def busca (vetor, esquerda, direita, pessoas):
  valor = int((esquerda + direita)/2)
  teste = testar(vetor, valor)
  if(esquerda == direita-1):
     return valor
  if(pessoas > teste):
    return busca(vetor, esquerda, valor, pessoas)
  else:
    return busca(vetor, valor, direita, pessoas)
  
#--------------------------------------------- MAIN
pessoas = int(input())
paes = int(input())
vetor = input().split()
vetor = list(map(int, vetor))
vetor = sorted(vetor)
#--------------------------------------------- ENTRADAS
resultado = 0
resultado = busca(vetor, vetor[0], vetor[len(vetor)-1], pessoas)
print(resultado)