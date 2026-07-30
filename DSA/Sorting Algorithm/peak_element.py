## Find Peak Element Using Binary Search 
def find_peak(arr): # TC:O(log n)
     n = len(arr)
     low = 0
     high = len(arr)-1

     while(low<=high):
          mid = low+(high-low)//2

          if((mid==0) or arr[mid-1]<arr[mid]) and ((mid==n-1) or arr[mid+1]<arr[mid]):
               return mid 
          elif( mid>0 and arr[mid-1] > arr[mid]):
               high = mid-1
          else:
               low = mid+1
     return -1 

arr = [1,2,3,0]
print(f"Peak Element:{find_peak(arr)}")
     