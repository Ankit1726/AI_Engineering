## Find Largest Element 

def largest(arr): # TC:O(n) & SC:O(1)
     n = len(arr)
     if(n<0):
          return 
     
     large = arr[0]
     for i in range(n):
          if(arr[i]>large):
               large = arr[i]
     return large

arr = [2,4,3,4,1,6,89,79,100]
print(largest(arr))
