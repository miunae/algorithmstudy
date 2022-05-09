import sys
N,r,c = map(int,sys.stdin.readline().split())
# r,c에 따라 2차원 배열을 4분면으로

answer = 0
while N != 0:
    N -= 1
    # 1사분면
    if r < 2**N and c < 2**N:
        answer += 0
    # 2사분면
    if r < 2**N and c >= 2**N:
        answer += (2**N) * (2**N) * 1
        # 한개 사분면 만큼 answer에 추가해주고 c 값을 사분면 하나가 되도록 빼준다.
        c -= (2**N)
    # 3사분면
    if r >= 2**N and c < 2**N:
        answer += (2**N) * (2**N) * 2
        r -= (2**N)
    # 4사분면
    if r >= 2**N and c >= 2**N:
        answer += (2**N) * (2**N) * 3
        r -= (2**N)
        c -= (2**N)
print(answer)