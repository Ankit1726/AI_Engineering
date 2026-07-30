## Cycle Sort 
def cycle_sort(arr): # TC:O(n) SC:O(1)
     i = 0
     n = len(arr)
     while(i<n):
          correct = arr[i]-1
          if(arr[i]!=arr[correct]):
               # Swap 
              arr[i],arr[correct] = arr[correct],arr[i]
          else:
               i+=1
     return arr

arr = [3,5,2,1,4]
print(cycle_sort(arr))