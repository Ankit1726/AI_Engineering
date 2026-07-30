## Fix Swap 2 elements
def fix_swap(arr):
     n = len(arr)
     first = second = -1
     for i in range(n-1):
          if(arr[i]>arr[i+1]):
               if(first==-1):
                    first = i
               second = i+1
     # Swap Identified Elements
     arr[first],arr[second] = arr[second],arr[first]

arr = [2,9,5,7,3,11]
print(f"Original Array:{arr}")
fix_swap(arr)
print(f"Sorted Array:{arr}")