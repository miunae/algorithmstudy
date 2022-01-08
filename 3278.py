import sys
n = int(input())
nums = sorted(list(map(int,sys.stdin.readline().split())))
x = int(input())
left = 0
right = n-1
cnt =0
while left < right: #왼쪽 오른쪽 인덱스부터 시작해서 인덱스에 변동주면서 찾아나선다.
    check = nums[left] + nums[right]
    if check == x:
        cnt += 1
        left += 1
    elif check < x:
        left += 1
    else:
        right -= 1
print(cnt)