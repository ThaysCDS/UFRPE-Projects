N, C = list(map(int, input().split()))

matriz = [[0 for i in range(C+1)] for i in range(N+1)]

for i in range(1, N+1):
  P, V = list(map(int, input().split()))
  for j in range(1, C+1):
    matriz[i][j] = V
    if P > j:
      matriz[i][j] = matriz[i-1][j]
    else:
      matriz[i][j] = max(matriz[i-1][j], matriz[i-1][j-P] + V)

print(matriz[N][C])
