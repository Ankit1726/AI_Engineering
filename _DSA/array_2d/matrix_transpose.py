## Transpose of matrix 
class Array_2D:

    def matrix_print(self,matrix):
        for rows in matrix:
            for values in rows:
                print(values,end=" ")
            print()

    def transpose(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        if not rows or not cols:
            return []

        res = [[0]* rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                res[j][i] = matrix[i][j]
        return self.matrix_print(res)

ans = Array_2D()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("Original Matrix")
ans.matrix_print(matrix)
print("Tranpose Matrix")
ans.transpose(matrix)