import heapq

def solution(scoville, K):
    tmp = 0
    count = 0
    scoville.sort()
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) != 1:
            tmp += scoville[0]
            heapq.heappop(scoville)
            tmp += heapq.heappop(scoville) * 2
            heapq.heappush(scoville, tmp)
            count += 1
            tmp = 0

        else:
            return -1
    return count