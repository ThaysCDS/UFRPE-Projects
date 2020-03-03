N = int(input())
cruzamentos = 0
c = 1
M = list(map(int, input().split()))

for i in range(len(M)-1, 0, -1):
    for j in range(len(M)-1-c, -1, -1):
        if M[j] > M[i]: 
          cruzamentos+=1
    c += 1

print(cruzamentos)
