def onibus(grafo, A, pai, dist, B):
  if (A == B):
    print(dist)
  for v in grafo[A]:
    if v != pai:
      onibus(grafo, v, A, dist+1, B)

N, A, B = list(map(int, input().split()))
A-=1
B-=1

dist = 0
pai = None

grafo = [[]for i in range(N)]

for c in range(N-1):
  P, Q = list(map(int, input().split()))
  P-=1
  Q-=1
  grafo[P].append(Q)
  grafo[Q].append(P)

onibus(grafo, A, pai, dist, B)
