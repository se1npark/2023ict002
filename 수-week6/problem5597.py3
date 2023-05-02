nums=list(range(1, 31))

for i in range(28):
    제출=int(input())
    nums.remove(제출)

nums.sort()
print(nums[0])
print(nums[1])