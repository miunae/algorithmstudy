import sys
from itertools import combinations
n = int(sys.stdin.readline())
nums = []
for i in range(1,11):   #최대 10자리니까 1~10자리 조합
    for comb in combinations(range(0,10),i):    # 0~9로 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str,comb))))
nums.sort()
if n <= len(nums)-1:
    print(nums[n])
else:
    print(-1)