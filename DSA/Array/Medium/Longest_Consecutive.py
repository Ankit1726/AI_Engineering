## Find Longest Consecutive Sequence 

class Solution:
     def find_consecutive(self,arr):  # TC: O(n) & SC:O(n)
          n = len(arr)
          my_set = set()

          for i in range(n):
               my_set.add(arr[i])

          longest = 0
          for num in my_set:
               if(num-1 not in my_set):
                    n = num
                    count = 1 
                    while(n+1 in my_set):
                         count+=1
                         n+=1

                    longest = max(longest,count)
          return longest


arr = [1,99,101,98,2,5,3,100,1,1]
sol = Solution()
ans = sol.find_consecutive(arr)
print(f"Longest COnsecutive Sequence Count: {ans}")
