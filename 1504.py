import sys
import heapq
INF = int(1e9)
N,E = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    distance =[INF]*(N+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance
v1, v2 = map(int,sys.stdin.readline().split())
original = dijkstra(1)
v1_path = dijkstra(v1)
v2_path = dijkstra(v2)
v1_first = original[v1] + v1_path[v2] + v2_path[N]
v2_first = original[v2] + v2_path[v1] + v1_path[N]
print(min(v1_first,v2_first) if min(v1_first,v2_first) < INF else -1)

