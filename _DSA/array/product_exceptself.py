## Calculate Product of Array Except Self 
class Array:
    def product_exceptSelf(self,nums):
        n = len(nums)
        ans = [1]*n

        # prefix 
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]


        # suffix 
        suffix = 1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans  

res = Array()
nums = [1,2,3,4]
print(res.product_exceptSelf(nums))