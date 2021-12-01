import sys
n = int(sys.stdin.readline())
Bcnt = [0]*n
building = list(map(int,sys.stdin.readline().strip().split()))
for i in range(n):
    MINH = -1000000000
    for j in range(i+1,n):
        slope = (building[j]-building[i]) / (j-i)
        if slope > MINH:
            MINH = slope
            Bcnt[i] += 1
            Bcnt[j] += 1
print(max(Bcnt))