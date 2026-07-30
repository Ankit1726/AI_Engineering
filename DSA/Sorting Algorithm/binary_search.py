## Binary Search

def binary_search(arr,target):
     low = 0
     high = len(arr)-1

     while(low<=high):
          mid = (low+high)//2
          
          if(arr[mid]==target):
               return "found"
          elif(arr[mid]<target):
               low = mid+1
          else:
               high = mid-1
     return "not found"

arr = [1,2,3,4,5]
target = 12
print(binary_search(arr,target))