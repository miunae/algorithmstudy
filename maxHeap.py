import sys
def insert(heap, num):
    heap.append(num)
    index = len(heap)-1
    while index > 1:
        if heap[index] > heap[index//2]:
            tmp = heap[index]
            heap[index] = heap[index//2]
            heap[index//2] = tmp
            index = index//2
        else: break
def remove(heap):
    ret = heap[1]
    tmp = heap.pop()
    parent = 1
    index = 2
    while index <= len(heap)-1:
        if index < len(heap)-1 and heap[index] < heap[index+1]:
            index += 1
        if heap[index] <= tmp:
            break
        heap[parent] = heap[index]
        parent = index
        index *= 2
    if len(heap) != 1:
        heap[parent] = tmp
    return ret

n = int(sys.stdin.readline())
command = []
heap = [None]
for _ in range(n):
    c = int(sys.stdin.readline())
    if c == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(remove(heap))
    else :
        insert(heap,c)
