'''
两个人取牌的数量不一定相等
而且不重复
暴利解题
'''

n = int(input())
numP =[([0] * 2) for i in range(n)]
numT =[]
for i in range(n):
    a, b = map(int, input().split())
    numP[i][0]=a
    numP[i][1]=b

print(numP)

def GetP(i,numP,numT):
    pass






