## Print Spiral Matrix 

from typing import List
class Matrix:
     def print_spiral(self,arr:List)-> List[int]: # TC:O(m × n)
          if not arr or not arr[0]:
               return []

          result = []
          left,right = 0,len(arr[0])-1
          top,bottom = 0,len(arr)-1
          while left<=right and top<=bottom:
               # Top fix 
               for i in range(left,right+1):
                    result.append(arr[top][i])
               top+=1

               # Right Fix 
               for i in range(top,bottom+1):
                    result.append(arr[i][right])
               right-=1

               if(top<=bottom):
                    for i in range(right,left-1,-1):
                         result.append(arr[bottom][i])
                    bottom-=1

               if(left<=right):
                    for i in range(bottom,top-1,-1):
                         result.append(arr[i][left])
                    left+=1
          return result

arr = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
     ]

sol = Matrix()
ans = sol.print_spiral(arr)
print(ans)