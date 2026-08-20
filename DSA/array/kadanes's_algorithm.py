## maximum subarray sum (kadane's algorithm)
class Array:
    def kadanes(self,arr):
        curr_sum = 0
        max_sum = float("-inf")
        n = len(arr)-1
        for i in range(n):
            curr_sum+=arr[i]
            max_sum = max(curr_sum,max_sum)
            if(curr_sum < 0):
                curr_sum = 0
        return max_sum

ans = Array()
arr = [3.-4,5,4,-1,7,-8]
print(ans.kadanes(arr))