## Linear search in an array
def linear_Search(arr,num): # TC:O(n) & SC:O(1)
     n = len(arr)
     if(n<0):
          return
     for i in range(n):
          if(arr[i]==num):
               return f"found at index:{i}"
     return f"not found"

arr = [7,4,5,8,7,9,10]
print(linear_Search(arr,9))