def countsort (V):

    m = 10000000 + 1
    aux = [0]*m
    for x in V:
        aux[x] += 1
    i = 0
    for z in range(m):
        for y in range(aux[z]):
            V[i] = z
            i += 1
            if (i == len(V)):
                break
    for t in V:
        print(t)



vetor = input()
vetor = vetor.split()
vetor = list(map(int,vetor))
countsort(vetor)


