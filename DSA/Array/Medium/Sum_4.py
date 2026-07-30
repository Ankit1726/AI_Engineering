## 4 Sum Problem 

class SOlution:
     def four_sum(self,arr,target):
          n = len(arr)  # TC:O(n^3)  SC:O(1)
          ans = []

          arr.sort()
          for i in range(n):
               # skip duplicates of i pointer 
               if i > 0 and arr[i] == arr[i-1]:
                    continue
               for j in range(i+1,n):
                    if j > i+1 and arr[j] == arr[j-1]:
                         continue

                    # intialise k and l pointer 
                    k = j+1 
                    l = n-1

                    while k<l: 
                         total = arr[i]+arr[j]+arr[k]+arr[l]

                         if total == target:
                              ans.append([arr[i],arr[j],arr[k],arr[l]])
                              k+=1
                              l-=1

                              while k<l  and arr[k] == arr[k-1]:
                                   k+=1

                              while k<l  and arr[k] == arr[k+1]:
                                   l-=1
                         elif total < target:
                              k+=1
                         else:
                              l-=1
          return ans 
          
     
arr = [-1,2,4,3,-3,8,3,9,7,-9,7,-4]
target = 0

sol = SOlution()
ans = sol.four_sum(arr,target)
print(ans)
               