## Find Next Permutation 

class Array:
    def nextPermutation(self,arr:list[int]):
        n = len(arr)
        pivot = -1 

        # find the pivot index 
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                pivot = i 
                break
        # if no pivot exists 
        if pivot == -1:
            arr.reverse()
            return
        # Find the element just larger than arr[pivot] and swap
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                # swap
                arr[pivot], arr[i] = arr[i], arr[pivot]
                break

        # reverse element after pivot 
        left,right = pivot+1,n-1 
        while left<right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1

res = Array()
arr = [1, 2, 3] # [1,2,3,5,4]
res.nextPermutation(arr)
print(arr)