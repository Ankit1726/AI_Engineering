## Remove Duplicates from Sorted Array 

from typing import List
class Solution:  # TC:O(n) & SC:(1)
     def remove_duplicates(self,arr:List[int]) -> int:
          n = len(arr)
          if (n<1):
               return 0
          i = 0
          j = i+1 
          while j<n:
               if(arr[j]!=arr[i]):
                    i+=1
                    # Swap
                    arr[j],arr[i] = arr[i],arr[j]
               j+=1
          return i+1

arr = [1,2,2,3,4,4,5,7,7,8]
sol = Solution()
ans = sol.remove_duplicates(arr)
print(f"Total Unique Elements: {ans}")