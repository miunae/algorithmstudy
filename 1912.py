from collections import deque
n = int(input())
nums = list(map(int,input().split()))
deq = deque(nums)
acc = 0 #축적
memory = max(deq)  #저장된 최대를 기록
while deq:
    x = deq.popleft()
    if x >= 0:
        acc += x
    else:
        if acc >= memory and acc>0:
            memory = acc
        if acc > abs(x):
            acc += x
        else :
            acc = 0
if acc != 0 and acc > memory:
    memory = acc

print(memory)