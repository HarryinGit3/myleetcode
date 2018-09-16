def calc(n, data):
    res = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (data[i][0]<data[j][0] and data[i][1]<data[j][1] and data[i][2]<data[j][2]):
                res = res+1
                break

    return res


n = int(input())
data = []
for i in range(0,n):
    raw = input().split(' ')
    line = []
    line.append(int(raw[0]))
    line.append(int(raw[1]))
    line.append(int(raw[2]))
    data.append(line)
res = calc(n, data)
print(res)
