'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
# 思路：遍历数组，找两个数的和，等于的话就返回
def twoSum(nums, target):
    lennums=len(nums)
    for i in range(lennums):
        for j in range(i+1,lennums):
            if nums[i]+nums[j] == target:
                return [i,j]
