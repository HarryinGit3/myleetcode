n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x1 = max(x) - min(x)
y1 = max(y) - min(y)
num = 0
if x1 > y1:
    num = x1
else:
    num = y1
print(num * num)