import sys
import math
N,M = map(int,sys.stdin.readline().split())
table = [[] for _ in range(N)]
for i in range(N):
    row = sys.stdin.readline().rstrip()
    for j in range(M):
        table[i].append(int(row[j]))
result = -1
# 1. 어느 행에서 시작하는가? 2. 어느 열에서 시작하는가?
# 3. 행에 적용되는 공차는?  4. 열에 적용되는 공차는?
# 위 4개 고려하여 가능한 수열을 추출하여 완전 제곱수 인지 판별
for n in range(N):
    for m in range(M):
        for ngap in range(-N,N):    # 행의 공차
            for mgap in range(-M,M):    # 열의 공차
                if ngap==0 and mgap ==0:    # 무한 루프 돌기 때문에 pass
                    continue
                x=n
                y=m
                cnt = 0
                value = ''
                # 수열 추출
                while(0<=x<N) and (0<=y<M):
                    value+=str(table[x][y])
                    cnt += 1
                #판별
                    value_int = int(''.join(value))
                    value_sqrt = math.sqrt(value_int)
                    value_decimal = value_sqrt - int(value_sqrt)
                    if value_decimal == 0 and value_int > result: result = value_int

                    x = n + cnt*ngap
                    y = m + cnt*mgap
print(result)