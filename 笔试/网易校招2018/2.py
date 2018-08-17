
a,b = map(int,input().split())
num =list(map(int, input().strip().split()))
times=0
maxI = []
minI = []
result = max(num) - min(num)

if result == 0 or a<0 or b<0:
    print(0,0)
else:
    while(b>=1):

        maxIndex=num.index((max(num)))
        minIndex=num.index(min(num))
        num[maxIndex]=num[maxIndex]-1
        num[minIndex]=num[minIndex]+1
        maxI.append(maxIndex)
        minI.append(minIndex)
        b=b-1
        times=times+1
        result = max(num)-min(num)
        if result==0:
            break
    print(result,times)
    length=len(maxI)
    for i in range(length):
        print(maxI[i]+1,minI[i]+1)


