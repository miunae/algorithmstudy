str1 = input().rstrip()
str2 = input().rstrip()
n = len(str1)
k = len(str2)
LCS = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if i==0 or j==0:    #index가 0인 줄이 있으면 모두 0
            LCS[i][j] = 0
        elif str1[i-1] == str2[j-1]:    #같을 시 대각선 다음 LCS의 값 +1
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
print(LCS[n][k])