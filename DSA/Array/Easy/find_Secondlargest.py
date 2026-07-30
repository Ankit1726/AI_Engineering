## Find Second Largest & Second Smallest

def second_largest(arr): #TC:O(n) & SC:O(1)
     n = len(arr)
     if(n<0):
          return

     largest = float("-inf")
     sec_largest = float("-inf")
     for i in range(n):
          if(arr[i]>largest):
               # Swap 
               sec_largest = largest
               largest = arr[i]
          elif (largest >arr[i]>sec_largest):
               sec_largest = arr[i]
     return [largest,sec_largest]


def second_smallest(arr):
     if(len(arr)<0):
          return

     smallest = float("inf")
     sec_smallest = float("inf")

     for i in arr:
          if(i<smallest):
               sec_smallest = smallest
               smallest = i 
          elif (smallest<i<sec_smallest):
               sec_smallest = i 
     return [smallest,sec_smallest]

arr = [2,4,3,16,7,8,9]
print(second_largest(arr))
print(second_smallest(arr))