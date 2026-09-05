## Linear SEarch in 2D Array
class Array_2D:
    def linear_search(self, matrix, key): # TC:O(R * C)
        rows = len(matrix)
        cols = len(matrix[0])
         
        if not rows or not cols:
            return "not found"
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == key:
                    return f"found values at: {(i,j)}"
        return f"not found."

    # row wise sum
    def row_sum(self,matrix):
        res = []
        for i in range(len(matrix)): # rows
            row_sum = 0 
            for j in range(len(matrix[0])):
                row_sum+=matrix[i][j]
            res.append(row_sum)
        return res


    # column wise sum
    def column_sum(self,matrix):
        res = []
        for j in range(len(matrix[0])): # cols 
            col_sum = 0 
            for i in range(len(matrix)): # rows 
                col_sum+=matrix[i][j]
            res.append(col_sum)
        return res


ans = Array_2D()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
search = ans.linear_search(matrix,key=5)
print(search)
print(f"Row Wise Sum: {ans.row_sum(matrix)}")
print(f"Column Wise Sum: {ans.column_sum(matrix)}")