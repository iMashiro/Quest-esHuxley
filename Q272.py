cont = 1
while True:
  try:
    if cont == 1:
      val1 = int(input())
      val2 = int(input())
      PROD = val1*val2
      cont = 2
    else:
      val1 = int(input())
      PROD *= val1
  except EOFError:
    print('Prod = ' + repr(PROD))
    break
