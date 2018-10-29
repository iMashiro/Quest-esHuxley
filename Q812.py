

def busca (left, right):
  if (left == right):
    if(soma[left] >= 0):
      return left, right, soma[left]
    else:
      return left, right, soma[left]
  else:
    somatorio = 0
    mid = int((left + right)/2)
    maximo_esquerda = -1e3
    esquerda = mid
    for i in range (mid, left-1, -1):
      somatorio += soma[i]
      if(somatorio >= maximo_esquerda):
        maximo_esquerda = somatorio
        esquerda = i

    maximo_direita = -1e3
    somatorio = 0

    direita = mid + 1
    for j in range(mid+1, right+1):
      somatorio += soma[j]
      if(somatorio >= maximo_direita):
        maximo_direita = somatorio
        direita = j
    
    ll, ml, a = busca(left,mid)
    mr, rr, b = busca(mid+1,right)
    c = maximo_direita + maximo_esquerda
    # print("%d (%d, %d) %d (%d, %d) %d (%d, %d)" % (a, ll, ml, b, mr, rr, c, esquerda, direita))

    if(a > b and a > c):
      return ll, ml, a
    elif(b > c and b > a):
      return mr, rr, b
    elif(c > a and c > b):
      return esquerda, direita, c
    elif (c == a and c == b):
      if (direita - esquerda > ml - ll and direita - esquerda > rr - mr):
        return esquerda, direita, c
      elif (ml - ll > direita - esquerda and ml - ll > rr - mr):
        return ll, ml, a
      else:
        return mr, rr, b
    elif (c == a):
      if (direita - esquerda > ml - ll):
        return esquerda, direita, c
      else:
        return ll, ml, a
    elif (c == b):
      if (direita - esquerda > rr - mr):
        return esquerda, direita, c
      else:
        return mr, rr, b
    else: #(a == b):
      if (ml - ll > rr - mr):
        return ll, ml, a
      else:
        return mr, rr, b

n = int(input())
contador = 1
while n != 0:
  dic = {}
  soma = []
  for i in range (n):
    dic[i] = []
  for i in range (n):
    A, B = map(int, input().split(' '))
    soma.append(A-B)
    dic[i].append((A,B))
  x, y, z = busca(0, n-1)
  if (z <= 0):
    print("Teste " + str(contador))
    print("nenhum")
    print()
  else:
    print("Teste " + str(contador))
    print(x+1, y+1)
    print()
  n = int(input())
  contador += 1

