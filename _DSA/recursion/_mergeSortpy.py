## Merge Sort 
class Merge_Sort: # TC:O(n*logn) & SC:O(n)
    def divide(self,arr:list[int],st:int,end:int) -> list[int]:
        if(st < end):
            # mid 
            mid = st+(end-st)//2 
            self.divide(arr,st,mid)    # left part 
            self.divide(arr,mid+1,end) # right part
            self.merge(arr,st,mid,end)

    def merge(self,arr,st,mid,end):
        temp = []
        i,j = st,mid+1 
        while(i<=mid and j<=end):
            if(arr[i]<arr[j]):
                temp.append(arr[i])
                i+=1 # left part 
            else:
                temp.append(arr[j])
                j+=1 # right part 

        # remaining left and right subarray element 
        while(i<=mid): # left 
            temp.append(arr[i])
            i+=1 
        while(j<=end): # right 
            temp.append(arr[j])
            j+=1 

        # add back into original array 
        for idx in range(0,len(temp)):
            arr[idx+st] = temp[idx]

    def print_arr(self,arr):
        for val in arr:
            print(val,end=" ")

    def merge_sort(self,arr):
        n = len(arr)
        if n>1:
           self.divide(arr,st=0,end=n-1)
           self.print_arr(arr)
    
obj = Merge_Sort()
arr = [12,31,35,8,32,17]
obj.merge_sort(arr)