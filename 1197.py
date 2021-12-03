import sys
import heapq    #프림 알고리즘: 현재 그래프에서 계속 짧은 경로 선택
INF = 22*(10**8)
v, e = map(int,sys.stdin.readline().split())
visited = [False]*(v+1)
Elist = [[] for _ in range(v+1)]
heap = [[0,1]]
for _ in range(e):
    s,end,w = map(int,sys.stdin.readline().split())
    Elist[s].append([w,end])
    Elist[end].append([w,s])

answer = 0
cnt = 0
while heap:
    if cnt == v:
        break
    w,s = heapq.heappop(heap)
    if visited[s] == False:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap,i)
print(answer)