### Matrix 2D 

class Matrix:
     def print_matrix(self,arr):
          rows = len(arr)
          cols = len(arr[0])

          for i in range(rows):
               for j in range(cols):
                    print(arr[i][j],end=" ")
               print()

     def upper_diagonal(self,arr):
          rows = len(arr)
          cols = len(arr[0])

          for i in range(rows):
               for j in range(cols):
                    if(j>=i):
                         print(arr[i][j],end=" ")
                    else:
                         print("*",end=" ")
               print()

     def lower_diagonal(self,arr):
               rows = len(arr)
               cols = len(arr[0])
     
               for i in range(rows):
                    for j in range(cols):
                         if(i>=j):
                              print(arr[i][j],end=" ")
                         else:
                              print("*",end=" ")
                    print()

     def print_diagonal(self,arr):
          rows = len(arr)
          cols = len(arr[0])

          for i in range(rows):
               for j in range(cols):
                    if(i==j):
                         print(arr[i][j],end=" ")
                    else:
                         print("*",end=" ")
               print()

     def print_transpose(self,arr):
          rows = len(arr)
          cols = len(arr[0])

          res = [[0]*rows for _ in range(cols)]
          for i in range(rows):
               for j in range(cols):
                    res[j][i] = arr[i][j]
          self.print_matrix(res)

arr = [[1,2,3],[3,4,5],[5,6,7]]
sol = Matrix()
sol.print_transpose(arr)