N, C, S = list(map(int, input().split()))
c = list(map(int, input().split()))

cs = [0 for i in range(N)]
cs[0] = 1

k = 0

for i in c:
  if i == 1:
    k+=1
    cs[k]+=1
  elif i == -1:
    k-=1
    cs[k]+=1

print(cs[S-1])
