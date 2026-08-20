## Linear Search in an array 
class Array:
    def linear_search(self,arr,target):
        n = len(arr)-1
        for i in range(0,n):
            if(arr[i]==target):
                return True
        return False

arr = [3,5,3,2,1,5,7,8]
ans = Array()
print(ans.linear_search(arr,5))