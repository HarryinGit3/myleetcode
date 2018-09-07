n, p1, p2, p3, t1, t2 = map(int, input().split())
l, r = map(int, input().split())
sum = (r - 1) * p1
while (n > 0):
    l2, r2 = map(int, input().split())
    mid = l2 - r
    p1pow = t1 * p1
    p2pow = t2 * p2
    if mid <= t1:
        sum = sum + mid * p1
    else:
        sum = sum + p1pow
        mid = mid - t1
        if mid <= t2:
            sum = sum + mid * p2
        else:
            sum = sum + p2pow + (mid - t2) * p3
    sum = sum + (r2 - l2) * p1
    l = l2
    r = r2
    n = n - 1
print(sum)