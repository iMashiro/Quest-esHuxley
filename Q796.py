def pot(n, exp):
  if (exp == 0):
    return 1
  elif (exp == 1):
    return n
  else:
    if (exp%2 == 0):
      resultado = pot(n, exp/2)
      return resultado*resultado
    else:
      resultado = pot(n, (exp - 1)/2)
      return resultado*resultado*n
while True:
  try:
    n1, n2 = map(int, input().split(' '))
    compot1 = pot(n1, n1) % 100
    compot2 = pot(n2, n2) % 100
    if (compot1 > compot2):
      n = n1
    elif (compot1 < compot2):
      n = n2
    else:
      n = 0
    print(n)
  except EOFError:
    break
