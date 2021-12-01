import sys
from collections import deque
n = int(sys.stdin.readline())
tree = list(map(int,sys.stdin.readline().split()))
delete = int(sys.stdin.readline())
child = [[] for _ in range(n)]
for i in range(n):
    if tree[i] == -1:
        continue
    child[tree[i]].append(i)
deq = deque()
deq.append(delete)
while deq:
    x = deq.popleft()
    for c in child[x]:
        deq.append(c)
    child[x]=[-1]
cnt = 0
for c in child:
    if c == [delete]:
        cnt += 1
    if len(c)==0:
        cnt+=1
print(cnt)