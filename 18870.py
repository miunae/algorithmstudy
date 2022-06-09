N = int(input())
nums = list(map(int,input().split()))
ans = [-1 for _ in range(N)]
dic = {}
for i in range(len(nums)):
    if nums[i] not in dic.keys():
        dic[nums[i]] = [i]
    elif nums[i] in dic.keys():
        dic[nums[i]].append(i)
nums = list(set(nums))
nums.sort()
for i in range(len(nums)):
    for idx in dic[nums[i]]:
        ans[idx] = i
for a in ans:
    print(a, end=' ')