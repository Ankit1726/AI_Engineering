## Set Matrix Zeroes

from typing import List
class Matrix:
     def print_matrix(self,arr): # TC:O(n*m) & SC:O(rows+cols)
          rows = len(arr)
          cols = len(arr[0])
          for i in range(rows):
               for j in range(cols):
                    print(arr[i][j],end=" ")
               print()

          
     def set_zeroes(self,arr:List[int]) -> List[int]:
          rows = len(arr)
          cols = len(arr[0])

          row_track = [0 for _ in range(rows)]
          col_track = [0 for _ in range(cols)]

          for i in range(rows):
               for j in range(cols):
                    if(arr[i][j] == 0):
                         row_track[i] = -1
                         col_track[j] = -1

          for i in range(rows):
               for j in range(cols):
                    if(row_track[i] == -1 or col_track[j] == -1):
                         arr[i][j] = 0
          self.print_matrix(arr)
                    

arr = [ [7,10,29,3],
        [1,20,0,4],
        [19,0,6,11],
        [4,27,14,7]
       
     ]
sol = Matrix()
sol.set_zeroes(arr)