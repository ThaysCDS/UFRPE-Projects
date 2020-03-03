#https://olimpiada.ic.unicamp.br/pratique/pu/2017/f2/papel/

N = int(input())
 
pedacos = (list(map(int,input().split(" "))))
 
p = len(pedacos)

if p != N:
  print("Quantidade de pedacos inválido, reinice o programa.")
else:
  corte_local = 2
  corte_global = 2

  n = len(pedacos)

  papeis = []

  for i in range(n):
    papeis.append((pedacos[i], i+1))

  papeis_ordenados = sorted(papeis)

  tesoura = [1 for i in range(n+2)]
  tesoura[0] = 0
  tesoura[n+1] = 0

  last = -1

  for i in papeis_ordenados:
    h, index =  i
    tesoura[index] = 0
    if last != h:
      if corte_local > corte_global:
        corte_local = corte_global
      last = h
    if tesoura[index-1] and tesoura[index+1]:
      corte_global+=1
    
  print(corte_global)
