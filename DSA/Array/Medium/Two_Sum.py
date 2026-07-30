## Two Sum Problem

from typing import List
class Solution:  # TC:O(n) & SC:O(n)
     def two_sum(self,arr:List[int],target:int) -> List[int]:
          n = len(arr)
          hash_map = {}

          for i in range(0,n):
               remain = target - arr[i]
               if remain in hash_map:
                    return[hash_map[remain],i]

               hash_map[arr[i]] = i

arr = [5,9,1,3,4,7,8]
target = 13
sol = Solution()
ans = sol.two_sum(arr,target)
print(ans)