import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    dis = y-x   # 거리
    cnt=0   # 이동 횟수
    move = 1    # 이동하는 거리
    total = 0   # 총 이동한 거리
    while total < dis:  # 이동한 거리가 실제 거리를 넘지 않을 때
        cnt += 1
        total += move
        if cnt%2 == 0:  #이동 횟수가 짝수일 때 이동할 거리를 1씩 증가
            move += 1
    print(cnt)