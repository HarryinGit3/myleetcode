n, k, t = map(int, input().split())
a = list(map(int, input().split()))
result = 0
for l in range(n - k + 1):
    r = l + k
    tempa = a[l:r]
    seta = set(tempa)
    dicta = {}
    for item in seta:
        dicta.update({item: tempa.count(item)})
    tempr = dicta.values()
    tt = max(tempr)
    if (int(t) <= tt):
        result = result + 1

print(result)