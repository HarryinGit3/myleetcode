'''

Author: Harryin

题目：在一个长度为n的数组里的所有数字都在0~n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次，
请找出数组中任意一个重复的数字。例如：如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3

要求：时间复杂度不超过O(n),空间复杂度为O(1)
'''


# 思路：通过排序或者哈希表并不能很好达到这个要求
# 通过对数组从头到尾扫描这个数组中的每个数字，当扫描到下标为i的数字时，首先比较这个数字（用m表示）是不是等于i。如果是，就扫描下一个，如果不是，就跟下标为m的数字比较，不相等就交换
# 交换之后再对比，如果不相同，再重复这个过程，直到找到。
def duplicate(number):
    # 如果数组长度小于等于1，返回False
    if (len(number) <= 1):
        return False
    # 如果数组范围超出0-n-1，返回False
    for item in number:
        if item < 0 or item > (len(number) - 1):
            return False
    length = len(number)
    for i in range(length):
        while(number[i]!=i):
            if(number[i]==number[number[i]]):
                return number[i]
                break
            temp = number[i]
            number[i] = number[temp]
            number[temp] = temp
    return False
number=[2,3,1,0,2,5,3]
result = duplicate(number)
if result == False:
    print("No one")
else:
    print(result)
