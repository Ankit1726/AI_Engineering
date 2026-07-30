## Find First & Last Element 
def first_last(arr,x):
     n = len(arr)  # TC:O(n)

     first = -1
     last = -1
     for i in range(n):
          if(x!=arr[i]):
               continue
          if(first==-1):
               first = i
          last = i 
     return [first,last]

# Optmial Appraoch Using Binary Search
class Solution:
    def First(self, arr: list, x: int) -> int:  # TC:O(log n)
        n = len(arr)
        low = 0
        high = n - 1
        res = -1
        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                res = mid 
                high = mid - 1  # Keep looking to the left
        return res
     
    def Last(self, arr: list, x: int) -> int:
        n = len(arr)
        low = 0
        high = n - 1
        res = -1
        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                res = mid 
                low = mid + 1  # Keep looking to the right
        return res
     
    def first_last(self, arr: list, x: int) -> list:
        # Notice the 'self.' prefix used here to call the class methods
        f = self.First(arr, x)
        l = self.Last(arr, x)
        return [f, l]
    
arr = [1,2,5,5,5,7,8,9]
x = 5
res = Solution()
ans = res.first_last(arr,x)
print(ans)