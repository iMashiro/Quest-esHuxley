parametros = input()
parametros = parametros.split()
casas = input()
casas = casas.split()
encomendas = input()
encomendas = encomendas.split()
parametros = list(map(int, parametros))
casas = list(map(int, casas))
encomendas = list(map(int, encomendas))
dicionario = {}
i = 0
while i < parametros[0]:
  dicionario[casas[i]] = i
  i += 1
i = 0
j = 0
contador = 0
while i < parametros[1]:
  if encomendas[i] != casas[j]:
    x = dicionario[encomendas[i]]
    k = j - x
    j = x
    if(k < 0):
      k *= -1
    contador += k
  i += 1

print(contador)
