def teste(aux2, chute):
  areatotal = 0
  for i in range (len(aux2)):
    if(aux2[i] >= chute):
      area = aux2[i]-chute
      areatotal += area*1
  return areatotal

def acharcorte(aux, comeco, fim, area):
  meio = (comeco + fim)/2
  resultadoteste = teste(aux, meio)
  if((fim - comeco) < 0.00001):
    return comeco
  if(area == resultadoteste):
    return meio
  elif(resultadoteste >= area):
    return acharcorte(aux, meio, fim, area)
  else:
    return acharcorte(aux, comeco, meio, area)

vetor = input()
vetor = vetor.split()
vetor = list(map(int,vetor))

while (vetor[0] != 0 and vetor[1] != 0):
  vetor2 = input()
  vetor2 = vetor2.split()
  vetor2 = list(map(int,vetor2))
  vetor2 = sorted(vetor2)  

  maior = 0
  menor = vetor2[0]
  for i in range (len(vetor2)):
    if(maior < vetor2[i]):
      maior = vetor2[i]
    if(menor > vetor2[i]):
      menor = vetor2[i]
  area = 0
  chute = int((maior+menor)/2)
  if(teste(vetor2, 0) == vetor[1]):
    print(":D")
  elif(teste(vetor2, 0) < vetor[1]):
    print("-.-")
  else:
    area = acharcorte(vetor2, 0, maior, vetor[1])  
    print("%.4f" %area)
  vetor = input()
  vetor = vetor.split()
  vetor = list(map(int,vetor))

