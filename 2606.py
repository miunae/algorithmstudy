import sys
N = int(sys.stdin.readline())
c = int(sys.stdin.readline())
table = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(c):
    i,j = map(int,sys.stdin.readline().split())
    table[i].append(j)
    table[j].append(i)
def dfs(n):
    visited[n] = True
    for i in table[n]:
        if visited[i] == False:
            dfs(i)
dfs(1)
print(visited.count(True)-1)