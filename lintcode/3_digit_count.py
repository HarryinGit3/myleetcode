"""
从0-n中数据寻找k(0-9)的数量
"""


def DigitCount(k, n):
    assert (n >= 0 and 0 <= k <= 9)
    cnt = 0
    for i in range(n + 1):
        j = i
        while True:
            if j % 10 == k:
                cnt += 1
            #//保证计算出来的是整数
            j //= 10
            if j == 0:
                break
    return cnt
