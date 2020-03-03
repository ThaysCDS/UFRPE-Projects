#https://olimpiada.ic.unicamp.br/pratique/p1/2017/f3/visita/

#funcao que calcula a menor distancia
def dijkstra(grafo, A, B):
  inicio = A - 1
  final = B - 1
  #atribui 'infinito' as distancias nao percorridas
  menor_distancia = [float('inf') for i in range(N)]
  #o caminho inical até ele mesmo, a distancia percorrida foi zero
  menor_distancia[inicio] = 0
  #vai salvando os caminhos e as distancias mínimas ja percorridas
  caminho = [(inicio, 0)]
  
 #enquanto  houver caminhos a serem percorridos na busca
  while caminho != []:
    no, peso = caminho.pop()
    for no_filho in grafo[no]:
      if menor_distancia[no_filho[0]] > no_filho[1] + peso:
        menor_distancia[no_filho[0]] = no_filho[1] + peso
        caminho.append((no_filho[0], menor_distancia[no_filho[0]]))
      
  return menor_distancia[final]

N, A, B = list(map(int, input().split()))

grafo = [[]for i in range(N)]

for c in range(N-1):
  P, Q, D = list(map(int, input().split()))
  P-=1
  Q-=1
  grafo[P].append((Q, D))
  grafo[Q].append((P, D))

print(dijkstra(grafo, A, B))
