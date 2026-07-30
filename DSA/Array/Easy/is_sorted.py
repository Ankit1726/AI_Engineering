## Check array is sorted or not
def isSorted(arr):  # TC:O(n) & SC:O(1)
     n = len(arr)  
     if(n<0):
          return 
     for i in range(0,n-1):
          if(arr[i]>arr[i+1]):
               return False
     return True

arr = [4,5,6,3,2,1]
print(isSorted(arr))