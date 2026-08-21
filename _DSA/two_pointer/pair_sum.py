## Pair Sum (given ans sorted array)
class Two_Pointer: # TC:O(n)
    def pair_sum(self,arr,target):
        n = len(arr)
        left,right = 0,n-1
        while(left<right):
            PS = arr[left]+arr[right]
            if(PS>target):
                right-=1
            elif(PS<target):
                left+=1
            else:
                return (arr[left],arr[right])
        return None

ans = Two_Pointer()
arr = [2,7,11,13,15]
print(ans.pair_sum(arr,target=9))