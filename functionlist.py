nums = [2,4,8,9,5]

nums.insert(1,3)
nums.remove(9)
nums.insert(0,nums.count(8))
for num in nums:
    print(num)
print(nums[2])