n = int(input())

a = list(map(int, input().split()))
if n < 1 or n > 100000:
    print(0)
else:
    length = len(a)
    sum = 0
    for i in range(length):
        for j in range(i + 1, length):
            tempA = a[i:j+1]
            maxA = max(tempA)
            minA = min(tempA)
            sum = sum + maxA - minA
print(sum)