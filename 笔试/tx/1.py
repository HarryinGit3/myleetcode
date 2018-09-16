def get_n(x, y):
    result = 0
    m = x + y
    for i in range(1, 21):
        result = i + result
        if (result > 21):
            i = i - 1
            return i


def get_r(n, x):
    r = 0
    c = 0
    if (x < n):

        for i in range(x, -1, -1):
            c = c + 1
            r = r + i
            if (r >= x):
                return c
    else:
        for i in range(n, -1, -1):
            c = c + 1
            r = r + i
            if (r >= x):
                return c

def get_num(n,x,y):
    r=0
    for i in range(n+1):
        r=r+i
    if(r!=(x+y)):
        return 0
    else:
        return 1


x, y = map(int, input().split())
result = get_n(x,y)
if(get_num(result,x,y)): 
    r = get_r(result, x)
    print(r)
else:
    print(-1)
