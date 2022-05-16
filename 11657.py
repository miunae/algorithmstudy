import sys
INF = int(1e9)
n,m = map(int,sys.stdin.readline().split())
edges = []
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append([a,b,c])
distance = [INF]*(n+1) # 최단 거리 테이블

def bellman_ford(start):
    distance[start] = 0 # 시작 노드
    # 정점의 수만큼 반복
    for i in range(n):
        # 반복 마다 모든 간선 확인
        for j in range(m):
            snode = edges[j][0] #starting node
            anode = edges[j][1] #arrive node
            cost = edges[j][2] # 거리
            # 기존의 최단 거리보다 짧다면 갱신
            if distance[snode] != INF and distance[anode] > distance[snode] + cost:
                distance[anode] = distance[snode]+cost
                # 음수 간선 순환을 확인(m번째에도 갱신된다면 음수 간선이 존재)
                if i == n-1:
                    return True
    return False
# 수행 후 음수 순환이 있다면 -1 출력
negative_cycle = bellman_ford(1)
if negative_cycle == True:
    print(-1)
else:
    for i in range(2,n+1):  # 첫번째 노드 제외
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])