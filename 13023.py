import sys
n,m = map(int,sys.stdin.readline().split())
rel = [[] for _ in range(n)]
visited = [False]*n
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    rel[a].append(b)
    rel[b].append(a)

def dfs(idx,cnt):
    if cnt == 4:
        print(1)
        exit()
    for i in rel[idx]:
        if visited[i] == False:
            visited[i] = True
            dfs(i,cnt+1)
            visited[i] = False
for i in range(n):
    visited[i] = True
    dfs(i,0)
    visited[i] = False
print(0)