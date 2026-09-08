## Print all subsets usng recursion 
class recursion:
    def subsets(self,arr:list[int],ans:list[int],i:int)-> list[int]:
        if(i==len(arr)):  # TC:O(n*2^n)
            print(ans)
            return
        # include 
        ans.append(arr[i])
        self.subsets(arr,ans,i+1)

        # bactrack step
        ans.pop()
        # exclude 
        self.subsets(arr,ans,i+1)

obj = recursion()
arr = [1,2,3]
ans = []
obj.subsets(arr,ans,i=0)