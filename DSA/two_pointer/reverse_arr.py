## Reverse an array
class Two_Pointer:
    def reverse_arr(self,arr):
        left,right = 0,len(arr)-1
        while(left<right):
            # swap 
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
        return arr

arr = [1,2,3,4,5,7,8]
ans = Two_Pointer()
print(ans.reverse_arr(arr))