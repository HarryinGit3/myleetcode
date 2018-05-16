"""
leetcode 766. Toeplitz Matrix
对矩阵判断，从左上角到右下角，看是否相等
"""

"""
思路：就是比较a[i][j]!=a[i+1][j+1]
"""
def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            if(matrix[i][j]!=matrix[i+1][j+1]):
                return False
        return True

nums=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
res=isToeplitzMatrix(nums)
print(res)