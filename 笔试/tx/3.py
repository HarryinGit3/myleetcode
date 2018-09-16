def triangleNumber(nums,x,y,z):
        rnum = 0
        bvld = False
        p1 = 0
        p2 = y
        p3 = z
        le = len(nums)
        for p1 in range(le - 2):
            for p2 in range(p1 + 1, le - 1):
                ma = nums[p1] + nums[p2]
                mi = abs(nums[p1] - nums[p2])
                for p3 in range(p2 + 1, le):
                    if nums[p3] in range(mi + 1, ma):
                        rnum += 1
                        #print(mi, ma)
                        #print(p1, p2, p3)
        return rnum

x, y, z = map(int, input().split())
nums=[]
for i in range(1,x+1):
    nums.append(i)
for i in range(1,y+1):
    nums.append(i)
for i in range(1,z+1):
    nums.append(i)
cnt = triangleNumber(nums)
print(cnt)

