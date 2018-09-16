import re
str1 = input()
str2 = input()

length = len(str2)
result = 0
for i in range(len(str1) - length + 1):
    tempstr = str1[i:i + length]
    set1=set(str1)
    set1=list(set1)
    for i in range(length):
        if(i<len(set1)):
            tempstr2 = tempstr.replace(str2[i],tempstr[i])
    if (tempstr2 == tempstr):
        result = result + 1
    print(tempstr)
print(result)