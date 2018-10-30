
def dp (atual, resto):
  if(memo[atual][resto] != -1):
    return memo[atual][resto]
  if (atual == N) or (resto == 0):
    memo[atual][resto] = 0
  elif (peso[atual] > resto):
    memo[atual][resto] = dp(atual+1, resto)
  else:
    memo[atual][resto] = max(valor[atual] + dp(atual+1, resto-peso[atual]), dp(atual+1, resto))
  return(memo[atual][resto])


N, P = map(int, input().split(' '))
memo = [[-1] * 10000 for i in range (100)]


valor = list(map(int, input().split(' ')))
peso = list(map(int, input().split(' ')))
print(dp(0, P))

