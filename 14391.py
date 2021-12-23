import sys
N,M = map(int,sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().strip())))

def bitmask():
    global maxAns
    for i in range(1 << N*M):   #bitmask로 2^n*m의 경우를 따져본다.
        total = 0
        #가로 합 계산
        for row in range(N):
            rowsum = 0
            for col in range(M):
                idx = row*M+col #idx는 2차원 배열을 1차원으로 옮겼을 때 인덱스 정보
                #가로일 때
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + arr[row][col]
                # 세로일 떄 앞에서 나온 수를 total에 합하고 rowum을 초기화
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum
        # 세로 합 계산
        for col in range(M):
            colsum = 0
            for row in range(N):
                idx = row*M + col
                # 세로일 때
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + arr[row][col]
                else :
                    total += colsum
                    colsum = 0
            total += colsum
        maxAns = max(maxAns,total)
maxAns = 0
bitmask()
print(maxAns)