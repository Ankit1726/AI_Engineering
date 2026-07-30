## Find Maximu Subarray Sum (Kadan's Algorithm)

class Solution:
     def Kadans(self,arr):
          n = len(arr)  # TC:O(n)
          total = 0 
          maxi = float("-inf")

          for i in range(n):
               total = total+arr[i]
               maxi = max(maxi,total)

               if(total <0):
                    total = 0
          return maxi

arr = [-2,1,-3,4,-1,2,1,-5,4]

sol = Solution()
ans = sol.Kadans(arr)
print(f"Maximum Subarray Sum: {ans}")