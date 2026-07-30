## Move Zeroes To End

from typing import List
class Solution: # TC:O(n) & SC:O(1)
     def moveZeroes(self,arr:List[int]) -> List[int]:
          n = len(arr)
          if(n<1):
               return
          i = 0 
          j = i+1 

          while (i<n):
               if(arr[i]==0):
                    break
               i+=1

               if(i==n):
                    return

               while(j<n):
                    if(arr[j]!=0):
                         # swap 
                         arr[i],arr[j] = arr[j],arr[i]
                         i+=1
                    j+=1
          return arr


arr = [1,0,0,3,0,4,5,0,0,7]
sol = Solution()
ans = sol.moveZeroes(arr)
print(ans)