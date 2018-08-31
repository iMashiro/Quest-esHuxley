def checar(vetor, teste):
  for i in range (len(vetor) - 1):
    if vetor[i + 1] - vetor[i] > teste:
      return 1
    elif vetor[i + 1] - vetor[i] == teste:
      teste = teste - 1
  return 0
casos = int(input())
for i in range(casos):
  passos = int(input())
  vetor = [0] + [int(k) for k in input().split(' ')]
  comeco = vetor[0]
  fim = vetor[len(vetor) - 1]
  menor = fim
  while comeco <= fim:
    meio = int((comeco + fim) / 2)
    if checar(vetor, meio) == 0:
      menor = meio
      fim = meio - 1
    else:
      comeco = meio + 1
  print("Case " + str(i+1) + ": " + str(menor))
