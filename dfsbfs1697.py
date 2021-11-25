from collections import deque
def bfs():
    deq = deque()
    deq.append(n)
    while deq:
        x = deq.popleft()
        if x == k:
            print(dist[x])
            break
        for i in (x-1,x+1,x*2):
            if  0<=i<=MAX  and dist[i] == 0:
                dist[i] = dist[x] + 1
                deq.append(i)

n,k = map(int,input().split())
MAX = 10**5
dist = [0]*(MAX+1)  #시간초과 방지
bfs()