## Find Missing Number 
def find_missing(arr):
     n = len(arr)  # TC:O(n)
     i = 0
     while i<len(arr):
          cor_idx = arr[i]
          if(arr[i]<n) and (arr[i]!=arr[cor_idx]):
               # Swap 
               arr[i],arr[cor_idx] = arr[cor_idx],arr[i]
          else:
               i+=1
     
     for i in range(n):
          if(arr[i]!=i):
               return i # return breakpoint 
     return n

arr = [4,0,2,1,5,7]
print(find_missing(arr))