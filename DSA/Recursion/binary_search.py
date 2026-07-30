## Binary Search Using Recursion
def binary(arr,left,right,target):
     if left>right:
          return -1
     # find mid 
     mid = left + (right-left)//2

     if(arr[mid]==target):
          return mid 
     
     elif(arr[mid]>target):
          return binary(arr,left,mid-1,target)
     else:
          return binary(arr,mid+1,right,target)
     
arr = [10,20,30,40,50,60,7]
n = len(arr)
target= 50
print(f"element index found at:{binary(arr,0,n,target)} ")