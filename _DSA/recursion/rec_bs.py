## binary search using recursion
class recursion: 
    def binary_seach(self,arr,tar,st,end): # TC:O(logn) & SC:O(logn)
        if(st<=end):
            mid = st+(end-st)//2 

            if(tar == arr[mid]):
                return mid 
            elif(arr[mid]<=tar):
                # search in 2nd half 
                return self.binary_seach(arr,tar,mid+1,end)
            else: 
                # search in first half 
                return self.binary_seach(arr,tar,st,mid-1) 

    def recursive_bs(self,arr,tar):
        st,end = 0,len(arr)-1
        return self.binary_seach(arr,tar,st,end)

obj = recursion()
arr = [1,3,5,7,9,11]
ans = obj.recursive_bs(arr,tar=7)
print(f"found at index:{ans}")