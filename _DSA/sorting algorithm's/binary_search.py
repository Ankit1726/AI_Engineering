## Binary Search Using Iteration Appraoch (array always sorted)
class Sorting:
    def binarySearch(self,arr,target): # TC:O(log n) & SC:O(1)
        st,end = 0,len(arr)-1 
        while(st<=end):
            # find mid 
            mid = st+(end-st)//2 
            if(target>arr[mid]):
                st = mid+1 # 2nd half 
            elif(target<arr[mid]):
                end = mid-1  # 1st half 
            else:
                return f"number found at index:{mid}"
        return -1 

    # uisnf recursion {not suitable due to SC:O(logn)}
    def recursionBS(self,arr,tar,st,end):
        if(st<=end):
            mid = st+(end-st)//2
            if(tar>arr[mid]):
                return self.recursionBS(arr,tar,mid+1,end)
            elif(tar<arr[mid]):
                return self.recursionBS(arr,tar,st,mid-1)
            else:
                return f"number found at index:{mid}"
        return -1 

ans = Sorting()
arr = [-1,0,3,4,6,7,9,12]
print(ans.binarySearch(arr,target=7))
print(ans.recursionBS(arr,tar=4,st=0,end=len(arr)-1))