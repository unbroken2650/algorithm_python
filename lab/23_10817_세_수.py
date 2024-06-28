nums = list(map(int, input().split()))
max_index = nums.index(max(nums))
min_index = nums.index(min(nums))

for i in [0, 1, 2]:
    if i != max_index and i != min_index:
        print(nums[i])
        break
