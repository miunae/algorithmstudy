import sys
from itertools import combinations
L,C = map(int,sys.stdin.readline().split())
moeum = ['a','e','i','o','u']   # 모음
nomi = sorted(sys.stdin.readline().rstrip().split())  # 후보 알파벳
result = []
cnt = 0
for no in list(combinations(nomi,L)):
    mocnt = jacnt = 0   #모음과 자음의 개수 카운트
    for c in no:
        if c in moeum:
            mocnt += 1
        else:
            jacnt += 1
    if mocnt > 0 and jacnt > 1: # 모음 1개 이상, 자음 2개 이상
        result.append("".join(no))
for pw in result:
    print(pw)