## Rotate Matrix By 90 Degree 

from typing import List
class Matrix:
     def print_matrix(self,matrix):
          rows = len(matrix)
          cols = len(matrix[0])
          for i in range(rows):
               for j in range(cols):
                    print(matrix[i][j],end=" ")
               print()

     def rotate(self,matrix:List[List[int]]):
          n = len(matrix)

          # Edge Case
          if not matrix or not matrix[0]: return []

          # Transpose Matrix
          for i in range(n-1):
               for j in range(i+1,n):
                    # Swap
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

          # Reverse Each Row
          for i in range(n):
               matrix[i].reverse()
          return self.print_matrix(matrix)
     
matrix = [
     [1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]
]

sol = Matrix()
ans = sol.rotate(matrix)
print(ans)