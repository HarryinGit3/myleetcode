nums = list(map(int, input().split()))
start = 0
nums2 = []
length = len(nums)
if length < 0:
    print(0)
elif length == 1:
    print(nums)
else:
    for i in range(1, length):
        if nums[i] < nums[start] :
            if len(nums2) == 0:
                start = i
                if i == len(nums):
                nums2.append(nums[start])
        else:
            nums2.append(nums[start])
            start = i
            if i == len(nums):
                nums2.append(nums[i])
        i = i + 1
print(sum(nums2))
