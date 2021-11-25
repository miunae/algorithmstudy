from collections import deque
def DFS(start):
    deq = deque()
    deq.append(start)
    while deq:
        x = deq.pop()
        if visited[x] == False:
            print(x, end=" ")
        visited[x] = True
        for i in adj[x]:
            if not visited[i]:
                deq.append(i)

def BFS(start):
    deq = deque()
    deq.append(start)
    while deq:
        x = deq.popleft()
        if visited[x] == False:
            print(x, end= " ")
        visited[x] = True
        for i in adj[x]:
            if not visited[i]:
                deq.append(i)

n, m, v = map(int,input().split())
adj = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
for i in range(len(adj)):
    adj[i].sort(reverse=True)
DFS(v)
print()
visited = [False]*(n+1)
for i in range(len(adj)):
    adj[i].sort()
BFS(v)