target = int(input())  # 목표 채널
M = int(input())  # 고장 버튼 수
out = list(map(int,input().split()))  # 고장난 버튼
answer = abs(100-target)  # 현재 채널에서 +,- 만 이용할 때

for nums in range(1000001):
    nums = str(nums)
    for i in range(len(nums)):
        if int(nums[i]) in out:
            break

        elif i == len(nums)-1:
            answer = min(answer, abs(int(nums)-target)+len(nums))

print(answer)