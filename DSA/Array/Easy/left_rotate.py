## Left Rotate Array By one 

from typing import List
class Solution: # TC:O(n) & SC:(1)
     def left_rotate(self,arr:List[int]) -> List[int]:
          temp = arr[0]
          n = len(arr)

          for i in range(n-1):
               arr[i] = arr[i+1]
          arr[n-1] = temp
          return arr

arr = [1,2,3,4,5]
sol = Solution()
ans = sol.left_rotate(arr)
print(ans)