commands = input().split('-')
answer = 0
tmp =[]
for com in commands:
    cnt = 0 # '-'로 묶는다.
    plus = com.split('+')
    for i in plus:
        cnt += int(i)
        # '-'로 묶은 값을 tmp에 저장
    tmp.append(cnt)
for i in range(1,len(tmp)):
    answer -= tmp[i]
# 맨 첫 숫자만 더해준다.
answer += tmp[0]
print(answer)