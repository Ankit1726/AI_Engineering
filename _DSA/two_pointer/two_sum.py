## 2 Sum Problem 
class Two_Pointer: #TC:O(n) & SC:(1)
    def two_sum(self,arr,tar):
        left = 0
        right = len(arr)-1 
        while (left < right):
            sum = arr[left]+arr[right]
            if(sum == tar):
                return [left,right] # returns index
            elif(sum<tar):
                left+=1 
            else:
                right-=1

arr = [1,4,3,2,5,7,8]
target = 8
ans = Two_Pointer()
print(ans.two_sum(arr,target))