pw = input()
k = int(input())
binary = bin(k-1)
bit = ""
answer = ""
cnt = 0
p=len(binary)-1 #비트 포인터
for i in pw:    # 가장 작은 경우
    if i == "1" or i == "2":
        cnt += 1
        bit += i
    elif i == "6":
        bit += "1"
        cnt += 1
    elif i == "7":
        bit += "2"
        cnt += 1
    else:
        bit += i
if k > 2**cnt:  # k가 바꿀 수 있는 비트 수보다 크면 -1
    answer = -1
else:
    for i in bit[::-1]:  # 수열을 뒤집는다.
        if i == "1":  # 숫자가 1이면
            if binary[p] == "1":  # 비트가 1이라면 뒤집는다
                answer = "6" + answer
                p -= 1
            elif binary[p] == "0":  # 비트가 0이면 pass
                answer = i + answer
                p -= 1
            else:
                answer = i + answer
        elif i == "2":
            if binary[p] == "1":
                answer = "7" + answer
                p -= 1
            elif binary[p] == "0":
                answer = i + answer
                p -= 1
            else:
                answer = i + answer
        else:
            answer = i + answer
print(answer)