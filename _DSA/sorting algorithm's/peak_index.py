## Peak Index in mountain array 
class Sorting:
    def peak_index(self,arr): # TC:O(logn)
        st,end=1,len(arr)-2
        while(st<=end):
            mid = st+(end-st)//2
            if(arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]):
                return mid 
            if(arr[mid-1]<arr[mid]): # increase --> search in right 
                st = mid+1 
            else: # decrease --> search in left 
                end = mid-1
        return -1 

res = Sorting()
arr = [0,3,8,9,5,2]
ans = res.peak_index(arr)
print(f"peak element:{arr[ans]}")