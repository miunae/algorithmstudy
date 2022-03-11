import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for i in range(n)]
dp = [(1,0),(0,1)]
MAX = max(li)
for i in range(2,MAX+1):
    if i > len(dp)-1:
        dp.append((dp[i-2][0]+dp[i-1][0],dp[i-2][1]+dp[i-1][1]))
for num in li:
    print(dp[num][0],end=' ')
    print(dp[num][1])
