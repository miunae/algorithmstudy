import sys
sys.setrecursionlimit(1000000)
n = int(input())
visited = [[False]*n for _ in range(n)]
graph = [[] for _ in range(n)]  #정상인
error = [[] for _ in range(n)]  #색맹
for i in range(n):
    r = sys.stdin.readline().rstrip()
    for j in range(n):
        graph[i].append(r[j])
        if r[j] == 'G': # 색맹일 시에 G는 R로 변경
            error[i].append('R')
        else:
            error[i].append(r[j])
cnt, errcnt = 0, 0
dx = [-1,1,0,0] # 상하좌우를 확인하기 위해
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = True
    cur = graph[x][y]
    for i in range(4):
        # X,Y는 상하좌우의 좌표
        X = x+dx[i]
        Y = y+dy[i]
        if (0 <= X < n) and (0<= Y < n):
            if visited[X][Y] == False:  #방문하지 않았고, 둘의 색상이 같을 때
                if graph[X][Y] == cur:
                    dfs(X,Y)
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            cnt += 1
print(cnt,end=' ')
# 색맹일 때
visited = [[False]*n for _ in range(n)]
graph = error.copy()
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            errcnt += 1
print(errcnt)