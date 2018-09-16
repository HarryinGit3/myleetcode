words=input("Input the words:")
l=words.split()  #使用空格分隔词语，得到各个单词\
nums=[]
for item in l:
   temp=item[::-1]
   nums.append(temp)
b=' '.join(nums)
print(b) 