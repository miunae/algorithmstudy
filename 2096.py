import sys
n = int(input())
a,b,c = map(int,sys.stdin.readline().split())
maxf = [a,b,c]
minf = [a,b,c]
for i in range(n-1):
    x,y,z = map(int,sys.stdin.readline().split())
    max0 = x+max(maxf[0],maxf[1])
    min0 = x+min(minf[0],minf[1])
    max1 = y+max(maxf[0],maxf[1],maxf[2])
    min1 = y+min(minf[0],minf[1],minf[2])
    max2 = z+max(maxf[1],maxf[2])
    min2 = z+min(minf[1],minf[2])
    maxf = [max0,max1,max2]
    minf = [min0,min1,min2]
print(max(maxf), min(minf))
