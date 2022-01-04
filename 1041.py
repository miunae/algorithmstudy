import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int,sys.stdin.readline().strip().split()))
sums=0
spaces = [] # 사용할 면의 최소값
if (n==1):
    nums = sorted(nums)
    sums = sum(nums)-nums[5]
else :
    # 마주 보고 있는 주사위 면 중 작은 면만
    spaces.append(min(nums[0],nums[5]))
    spaces.append(min(nums[1],nums[4]))
    spaces.append(min(nums[2],nums[3]))
    spaces.sort()
    # 1,2,3면이 보이는 주사위의 최소 합
    space1 = spaces[0]  # 한 면만 보이는 주사위는 무조건 제일 작은 면
    space2 = spaces[0]+spaces[1]
    space3 = spaces[0]+spaces[1]+spaces[2]
    # 1,2,3면이 보이는 주사위의 개수
    n1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    n2 = 4*(n-2) + 4*(n-1)
    n3 = 4
    sums += n1 * space1
    sums += n2 * space2
    sums += n3 * space3
print(sums)
