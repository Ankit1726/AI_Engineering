## Merge Sort 
def merge_sort(arr): # TC:O(nlog n) SC:O(n)
     if(len(arr)<=1):
          return arr
     mid = len(arr)//2
     left_half = arr[:mid]
     right_half = arr[mid:]

     merge_sort(left_half)
     merge_sort(right_half)
     merge(arr,left_half,right_half)
     return arr 

# Merging Function
def merge(arr,left_half,right_half):
     i = j = k = 0 

     while(i<len(left_half) and j<len(right_half)):
          if(left_half[i]<right_half[j]):
               arr[k] = left_half[i]
               i+=1
          else:
               arr[k] = right_half[j]
               j+=1
          k+=1
          
     # any element remains 
     while(i<len(left_half)):
          arr[k] = left_half[i] # left part check
          i+=1
          k+=1
          
     while(j<len(right_half)):
          arr[k] = right_half[j]  # right part check   
          j+=1
          k+=1
     return arr

arr = [3,2,1,4,5,6,8,7,3]
print(merge_sort(arr)) 