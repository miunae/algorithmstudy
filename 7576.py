import sys
from collections import deque
m,n = map(int,sys.stdin.readline().split())
table = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
day = 0
deq = deque([])
# 상하좌우 좌표에서 이동을 위한 리스트
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 토마토의 인덱스를 큐에 삽입
for i in range(n):
    for j in range(m):
        if table[i][j] == 1:
            deq.append([i,j])
# 너비 우선 탐색
while deq:
    x,y = deq.popleft()
    for i in range(4):
        nx,ny = dx[i]+x, dy[i]+y #상하좌우 좌표
        # 주변의 토마토가 익지 않았으면 익혀주고 1일 추가, 인덱스가 초과되거나 작게 되면 안됨
        if 0<=nx<n and 0<=ny<m and table[nx][ny] == 0:
            table[nx][ny] = table[x][y]+1
            deq.append([nx,ny])
for i in range(n):
    for j in range(m):
        if table[i][j] == 0:
            print(-1)   # 익지 않은 곳이 있을 때
            exit(0)
    # 테이블 내 최대값 -1이 정답
    day = max(day,max(table[i]))
print(day-1)