## Search in Rotated Sorted Array 
class Sorting:
    def roated_BS(self,arr,target): # TC:O(logn)
        st,end = 0,len(arr)-1
        while(st<=end):
            mid = st+(end-st)//2 
            if(arr[mid]==target):
                return mid 

            if(arr[st]<arr[mid]): # left sorted 
                if(arr[st]<=target and target<=arr[mid]):
                    end = mid-1
                else:
                    st = mid+1
            else: # right sorted 
                if(arr[mid]<=target and target<=arr[end]):
                    st = mid+1 
                else:
                    end = mid-1
        return -1 

res = Sorting()
arr = [3,4,5,6,7,0,1,2]
ans = res.roated_BS(arr,target=5)
print(f"found at index:{ans}")