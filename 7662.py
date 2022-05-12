import sys
import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    maxheap = []
    minheap = []
    visited = [0]*k #삭제 여부 확인
    for i in range(k):
        exp, num = sys.stdin.readline().split()
        num = int(num)
        if exp == 'I':
            heapq.heappush(maxheap,(-1*num,i))
            heapq.heappush(minheap,(num,i))
        elif exp == 'D' and num == -1:
            while minheap:
                if visited[minheap[0][1]] == 1:
                    heapq.heappop(minheap)
                else:
                    break
            if minheap:
                min = minheap[0][1]
                visited[min] = 1
                heapq.heappop(minheap)

        elif exp == 'D' and num == 1:
            while maxheap:
                if visited[maxheap[0][1]] == 1:
                    heapq.heappop(maxheap)
                else:
                    break
            if maxheap:
                max = maxheap[0][1]
                visited[max] = 1
                heapq.heappop(maxheap)
    while minheap:
        if visited[minheap[0][1]] == 1:
            heapq.heappop(minheap)
        else:
            break
    while maxheap:
        if visited[maxheap[0][1]] == 1:
            heapq.heappop(maxheap)
        else:
            break
    if minheap:
        print((-1)*maxheap[0][0],minheap[0][0])
    else:
        print('EMPTY')