## Check array is sorted and rotated 

from typing import List # TC:O(n)
class Solution:
     def check(self,arr:List[int]) -> bool:
          n = len(arr)

          rotations = 0
          for i in range(0,n):
               if(arr[i]>arr[(i+1)%n]):
                    rotations+=1
               if rotations > 1:
                    return False
          return True

arr = [4,5,1,2,3]
sol = Solution()
ans = sol.check(arr)
print(ans)