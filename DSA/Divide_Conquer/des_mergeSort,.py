# Descending Merge Sort 
def des_mergeSort(arr):
     if(len(arr)<=1):
          return arr
     if(len(arr)>1):
          mid = len(arr)//2
          left = arr[mid:]
          right = arr[:mid] # divide into 2 halves

          des_mergeSort(left)
          des_mergeSort(right)
          merge(arr,left,right)
     return arr 

def merge(arr,left,right):
     i = j = k = 0
     while(i<len(left) and j<len(right)):
          if(left[i]>right[j]):
               arr[k] = left[i]
               i+=1 
          else:
               arr[k] = right[j]
               j+=1
          k+=1
     
     # Remaining Element 
     while(i<len(left)): # left remaining element
          arr[k] = left[i]
          i+=1
          k+=1
     
     while(j<len(right)): # right remaining element 
          arr[k] = right[j]
          j+=1
          k+=1


arr = [3,2,1,5,4,3,5,6]
print(des_mergeSort(arr))
