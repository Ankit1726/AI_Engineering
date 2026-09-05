## 2D Array 
class Array_2D:
    def traverse(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        if not rows or not cols:
            return

        for i in range(rows):
            for j in range(cols):
                print(matrix[i][j],end=" ")
            print()

        # for row in matrix:
        #     for value in row:
        #         print(value,end=" ")
        #     print()

res = Array_2D()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res.traverse(matrix)