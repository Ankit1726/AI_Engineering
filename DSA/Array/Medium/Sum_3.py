## 3 Sum Problem

from typing import List
class Solution:
     def three_sum(self,arr:list[int]) -> List[List[int]]:
          ans = []
          n = len(arr)  # TC:O(n^2) & SC:O(1)

          # sort array 
          arr.sort()

          # fix i ppinter 
          for i in range(n):
               # skip duplicates --> i 
               if i > 0 and arr[i] == arr[i-1]:
                    continue

               # initialise j and k 
               j = i+1
               k = n-1

               while j<k:
                    sum = arr[i]+arr[j]+arr[k]

                    if sum < 0:
                         j+=1
                    elif sum > 0:
                         k-=1 
                    else: # found triplet 
                         temp = [arr[i],arr[j],arr[k]]
                         ans.append(temp)

                         j+=1
                         k-=1

                         # Skip duplicates --> j 
                         while j<k and arr[j] == arr[j-1]:
                              j+=1

                         # skip duplicates --> k 
                         while j<k  and arr[k] == arr[k+1]:
                              k-=1
          return ans

arr = [-1,-1,3,2,1,4,3,-2,3,-3]
sol = Solution()
ans = sol.three_sum(arr)
print(ans)