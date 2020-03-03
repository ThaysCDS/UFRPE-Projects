#https://olimpiada.ic.unicamp.br/pratique/p2/2017/f2/frete/

def frete(cidades, O, N):
    inicio = O-1
    fim = N-1
    custo = [float('inf') for i in range(M)]
    custo[inicio] = 0
    trajeto = [(inicio, 0)]
    while trajeto != []:
        cid, preco = trajeto.pop()
        for frt in cidades[cid]:
            if custo[frt[0]] > frt[1] + preco:
                custo[frt[0]] = frt[1] + preco
                trajeto.append((frt[0], custo[frt[0]]))
    return custo[fim]

N, M = list(map(int, input().split()))
O = 1
cidades = [[] for i in range(M-1)]
 
for i in range(M):
    A, B, C = list(map(int, input().split()))
    A-=1
    B-=1
    cidades[A].append((B, C))
    cidades[B].append((A, C))

print(frete(cidades, O, N))
