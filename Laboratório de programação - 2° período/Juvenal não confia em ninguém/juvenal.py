def explora(m,navios, i, j, pos):

  if m[i-1][j] == '#':
    navios[pos].append((i-1, j))
    m[i-1][j] = '.'
    explora(m, navios, i-1, j, pos)
    
  if m[i][j-1] == '#':
    navios[pos].append((i, j-1))
    m[i][j-1] = '.'
    explora(m, navios, i, j-1, pos)

  if m[i+1][j] == '#':
    navios[pos].append((i+1, j))
    m[i+1][j] = '.'
    explora(m, navios, i+1, j, pos)

  if m[i][j+1] == '#':
    navios[pos].append((i, j+1))
    m[i][j+1] = '.'
    explora(m, navios, i,j+1, pos) 

N, M = list(map(int, input().split()))

m = []
m.append(['.' for i in range(M+2)])

for i in range(1, N+1):
  temp = ' '.join(input()).split()
  m.append(['.']+ temp +['.'])

m.append(['.' for i in range(M+2)])

pos = 0
c = 0
n = len(m)

navios = []

for i in range(1, n):
  for j in range(1, M+1):
    if m[i][j] == '#':
      m[i][j] = '.'
      navios.append([(i, j)])
      explora(m, navios, i, j, pos) 
      pos+=1
  
disparos = []

K = int(input())
for j in range(K):
  L, C = list(map(int, input().split()))
  disparos.append((L, C))

for i in range(len(disparos)):
  for j in range(len(navios)):
    if disparos[i] in navios[j]:
      navios[j].remove(disparos[i])

for i in navios:
  if i == []:
    c+=1

print(c)
