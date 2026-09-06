## Search in 2D Matrix Variation-2

class Array_2D:
    def searchMatrix(self,matrix,target): # TC:O(m+n)
        m = len(matrix)
        n = len(matrix[0])

        row,col = 0,n-1
        while(col>=0 and row<m):
            if(target == matrix[row][col]):
                return True
            elif(target<matrix[row][col]):
                col-=1 # goes to left 
            elif(target>matrix[row][col]):
                row+=1 # goes down 
        return False

obj = Array_2D()
matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
print(obj.searchMatrix(matrix,target=5))