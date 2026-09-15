class array:
    def sum_4(self,arr:list[int],tar:int)-> list[list[int]]:
        ans = []
        n = len(arr) # TC:O(nlogn+n^3)

        # sort array 
        arr.sort()

        for i in range(n):
            # skip duplicates of i 
            if(i>0 and arr[i]==arr[i-1]):
                continue
            for j in range(i+1,n):
                # skip duplicates of j 
                if(j>i+1 and arr[j]==arr[j-1]):
                    continue

                # apply 2 pointer 
                p,q = j+1,n-1
                while p<q:
                    sum = arr[i]+arr[j]+arr[p]+arr[q]
                    if(sum<tar):
                        p+=1 
                    elif(sum>tar):
                        q-=1 
                    else:
                        ans.append([arr[i],arr[j],arr[p],arr[q]])
                        p+=1
                        q-=1 

                        # skip duplicates of p 
                        while p<q and arr[p]==arr[p-1]:
                            p+=1 
        return ans 

obj = array()
arr = [-2,-1,-1,1,1,2,2]
print(obj.sum_4(arr,tar=0))