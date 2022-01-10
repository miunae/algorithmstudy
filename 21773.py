import sys
import heapq
T,n = map(int,sys.stdin.readline().split())
process = []
for i in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    heapq.heappush(process,[-c,a,b])
for _ in range(T):
    cur = heapq.heappop(process)
    print(cur[1])
    # 나머지 우선순위가 상승하는 것은 나의 우선순위가 1 감소하는 것과 마찬가지(-부호 붙였으므로 +1)
    if cur[2] > 1:
        heapq.heappush(process,[cur[0]+1,cur[1],cur[2]-1])
