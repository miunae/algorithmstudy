import sys

n,m = map(int,sys.stdin.readline().split())
dic = {}
for _ in range(n):
    a=sys.stdin.readline().strip()
    if a not in dic.keys():
        dic[a]=1
    else:
        dic[a]+=1
k = int(input())
max = 0
for key,value in dic.items():
    zero = key.count('0')
    if k == zero:
        if value >= max:
            max = value
    elif k < zero:
        continue
    elif k > zero:
        if (k-zero)%2==0:
            if value >= max:
                max = value
print(max)