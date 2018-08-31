def simpleMerge(a, b):
    total = len(a) + len(b)
    j, k = 0, 0
    
    c = list()
    global contador
    for i in range(total):
      if (k == len(b) or (j < len(a) and a[j] <= b[k])):
          c.append(a[j])
          j += 1
      else:
          c.append(b[k])
          contador = contador + ((total - (len(b))) - j)
          k += 1
    return(c)

def mergeSort(data):
    if (len(data) <= 1):
        return(data)

    middle = int(len(data) / 2)
    left = mergeSort(data[0 : middle]) # O data de 0 at� middle
    right = mergeSort(data[middle : len(data)]) # O data de middle at� o final

    result = simpleMerge(left, right)
    return(result)


casos = input()
casos = int(casos)
i = 0
contador = 0
while True:
  try:
    vetor = []
    x = input()
    if(x != ''):
      while(x != ''):
        vetor.append(int(x))
        x = input()
      vetor2 = list(map(int,vetor))
      del vetor2[0]  
      mergeSort(vetor2)
      print(contador)
      contador = 0
    
  except EOFError:
    vetor2 = list(map(int,vetor))
    del vetor2[0]
    mergeSort(vetor2)
    print(contador)
    contador = 0
    break



