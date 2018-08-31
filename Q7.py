valor1 = float(input())
valor2 = float(input())
op = input()
x = valor1
while op != '&':
  if op == '+':
    x += valor2
    print("%.3f" % x)
  elif op == '-':
    x -= valor2
    print("%.3f" % x)
  elif op == '*':
    x *= valor2
    print("%.3f" % x)
  elif op == '/':
    if valor2 == 0:
      print("operacao nao pode ser realizada")
    else:
      x /= valor2
      print("%.3f" % x)
  valor2 = float(input())
  op = input()
