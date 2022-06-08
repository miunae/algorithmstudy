import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
miro = []
for _ in range(N):
    row = sys.stdin.readline().rstrip()
    row = list(map(int,row))
    miro.append(row)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

deq = deque()
deq.append([0,0])
while deq:
    x,y = deq.popleft()
    # 인접한 칸 확인
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and miro[nx][ny] ==1:
            if nx==0 and ny==0:
                continue
            miro[nx][ny] = miro[x][y]+1
            deq.append([nx,ny])
print(miro[N-1][M-1])