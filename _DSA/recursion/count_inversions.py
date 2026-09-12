## Count Inversion Pairs 
class backtrack: # TC:O(n*logn) & SC:O(n)

    def frequency(self,arr:list[int],st:int,mid:int,end:int) -> int:
        temp = []
        i,j = st,mid+1 
        invCount = 0 

        while(i<=mid and j<=end):
            if(arr[i]<=arr[j]):
                temp.append(arr[i])
                i+=1 
            else:
                temp.append(arr[j])
                j+=1
                invCount+=(mid-i+1)

        while(i<=mid):
            temp.append(arr[i])
            i+=1 
        while(j<=end):
            temp.append(arr[j])
            j+=1 

        for idx in range(len(temp)):
            arr[idx+st] = temp[idx]
        return invCount
    
    def countInversion(self,arr:list[int],st:int,end:int):
        if(st>=end):
            return 0
        
        if(st<end):
            mid = st+(end-st)//2 
            left_count = self.countInversion(arr,st,mid)
            right_count = self.countInversion(arr,mid+1,end)
            inv_freq = self.frequency(arr,st,mid,end)
        return left_count + right_count + inv_freq
          
        return 0

obj = backtrack()
arr = [6,3,5,2,7]
ans = obj.countInversion(arr,st=0,end=len(arr)-1)
print(f"Total Pair Count:{ans}")