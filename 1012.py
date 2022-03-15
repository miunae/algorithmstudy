from collections import deque
dx=[-1,0,1,0]
dy=[0,-1,0,1]
T=int(input())
for _ in range(T):
    n,m,k=map(int,input().split())
    a=[[0]*m for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        a[x][y]=1
    q=deque()
    cnt=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                a[i][j]=0
                q.append((i,j))
                while q:
                    px, py = q.popleft()
                    for k in range(4):
                        nx=px+dx[k]
                        ny=py+dy[k]
                        if nx<0 or nx>=n or ny<0 or ny>=m:
                            continue
                        if a[nx][ny]==1:
                            a[nx][ny]=0
                            q.append((nx,ny))
                cnt+=1
    print(cnt)