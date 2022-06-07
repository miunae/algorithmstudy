import re
# (100 ~ 1 ~ | 01) ~
signal = input()
# 패턴 컴파일
pattern = re.compile('(100+1+|01)+')
ans = pattern.fullmatch(signal)

if ans:
    print("SUBMARINE")
else:
    print("NOISE")