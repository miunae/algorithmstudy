import sys
import heapq
n = int(input())
set = [int(sys.stdin.readline()) for i in range(n)]
heapq.heapify(set)
cnt = 0
if len(set) == 1:
    print(0)
else:
    while len(set) > 1:
        card1 = heapq.heappop(set)
        card2 = heapq.heappop(set)
        sum = card1 + card2
        cnt += sum
        heapq.heappush(set,sum)
    print(cnt)
