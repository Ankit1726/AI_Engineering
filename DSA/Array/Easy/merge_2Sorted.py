## Merge @ Sorted Array 
def merge_arr(arr1,arr2): # TC:O(n+m) & SC:O(n+m)
     n = len(arr1)
     m = len(arr2)
     result = []

     i,j = 0,0
     while i<n and j<m:
          if(arr1[i]<arr2[j]):
               result.append(arr1[i])
               i+=1
          else:
               result.append(arr2[j])
               j+=1

     # remaining elments
     while(i<n):
          result.append(arr1[i])
          i+=1
     while(j<m):
          result.append(arr2[j])
          j+=1

     return result

arr1 = [1,3,4,7]
arr2 = [2,5,6,8]
print(merge_arr(arr1,arr2))