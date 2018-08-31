parametros = input()
parametros = parametros.split()
casas = input()
casas = casas.split()
encomendas = input()
encomendas = encomendas.split()
parametros = list(map(int, parametros))
casas = list(map(int, casas))
encomendas = list(map(int, encomendas))

x = 0
i = 0
j = 0
contador = 0
while i < parametros[1]:
  if (encomendas[i] < casas[j]):
    while encomendas[i] != casas[j]:      
      j -= 1
      contador += 1
  elif(encomendas[i] > casas[j]):
    while encomendas[i] != casas[j]:
      j += 1
      contador += 1
  i += 1

print (contador)
