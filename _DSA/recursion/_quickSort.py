## Quick Sort 
class Quick_Sort: # TC:O(n*logn) & SC:O(1)

    def partition(self,arr:list[int],st:int,end:int) -> int:
        idx = st-1 
        pivot = arr[end]
        # place els <= pivot (left of pivot)
        for j in range(st,end):
            if(arr[j]<=pivot):
                idx+=1
                # swap j --> idx 
                arr[j],arr[idx] = arr[idx],arr[j]

        # place pivot at right pos 
        idx +=1 
        arr[end],arr[idx] = arr[idx],arr[end]
        return idx      

    def quickSort(self,arr:list[int],st:int,end:int):
        # base case 
        if(st>=end):
            return

        pivIdx = self.partition(arr,st,end)
        self.quickSort(arr,st,pivIdx-1) # left cal
        self.quickSort(arr,pivIdx+1,end) # right cal

    # print array 
    def print_arr(self,arr):
        for val in arr:
            print(val,end=" ")

obj = Quick_Sort()
arr = [5,2,6,4,1,3]
obj.quickSort(arr,st=0,end=len(arr)-1)
obj.print_arr(arr)