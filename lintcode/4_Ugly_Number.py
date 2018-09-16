"""
丑数，只含因子2,3,5的第n大的数
"""


def nthUglyNumber(n):
    if n <= 1:
        return n

    factors = [2, 3, 5]
    heap = factors +[1]
    