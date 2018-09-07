n,m = map(int,input().split())
flowers = list(map(int,input().split()))
Q = int(input())

def GetResult(fls,l,r):
    newfls = fls[l:r]
    set1 = set(newfls)
    return len(set1)


result = []
for i in range(Q):
    tl,tr = map(int,input().split())
    tl=tl-1
    result.append(GetResult(flowers,tl,tr))

for item in result:
    print(item)



