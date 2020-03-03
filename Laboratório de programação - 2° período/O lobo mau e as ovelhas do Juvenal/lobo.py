import sys

sys.setrecursionlimit(10000)

def cercado(c, i, j):
    if c[i][j] == "#":
        return
    if c[i][j] == "k":
        global rebanho
        rebanho += 1
    if c[i][j] == "v":
        global alcateia
        alcateia += 1
    if c[i][j] != "#":
      c[i][j] = "#"

    cercado(c, i-1, j)
    cercado(c, i+1, j)
    cercado(c, i, j-1)
    cercado(c, i, j+1)

R, C = list(map(int, input().split()))

if (R < 3 and R > 250) or (C < 3 and C > 250):
  print('Valor inválido!')

c = []
c.append(['#' for i in range(C+2)])

for i in range(1, R+1):
  temp = ' '.join(input()).split()
  c.append(['#']+ temp +['#'])

c.append(['#' for i in range(C+2)])

ovelha = 0
lobo = 0

for i in range(1,R+1):
    for j in range(1,C+1):
      rebanho = 0
      alcateia = 0
      cercado(c, i, j)
      if rebanho > alcateia:
        ovelha += rebanho
        alcateia = 0
      else:
        lobo += alcateia
        rebanho = 0

print("%s %s" % (ovelha, lobo))
