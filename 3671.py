import sys
import math
from itertools import permutations
def prime(n):  # 소수인지 판별
    if n == 0 or n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

c = int(sys.stdin.readline())
case = [[] for _ in range(c)]
for i in range(c):
    a = sys.stdin.readline().rstrip()
    for j in a:
        case[i].append(j)
for cs in case:
    cnt = 0
    permu = set()
    for i in range(1,len(cs)+1):
        per = set(permutations(cs,i))
        permu.update(per)
    permu = list(permu)
    for j in range(len(permu)):
        permu[j] = "".join(permu[j])
    permu = set(map(int, permu))
    for p in permu:
        if prime(p) == True:
            cnt += 1
    print(cnt)