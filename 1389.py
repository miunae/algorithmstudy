from collections import deque
N,M = map(int,input().split())
answer = [[idx,0] for idx in range(N+1)]
rel = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    rel[a].append(b)
    rel[b].append(a)
for idx in range(1,N+1):
    visited = [0]*(N+1)
    deq = deque()
    deq.append(idx)
    while deq:
        cur = deq.popleft()
        for adj in rel[cur]:
            if visited[adj] == 0 and adj != idx:
                deq.append(adj)
                visited[adj] = visited[cur]+1
    answer[idx][1] = sum(visited)
answer = sorted(answer,key = lambda x: (x[1],x[0]))
print(answer[1][0])