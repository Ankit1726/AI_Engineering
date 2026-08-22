## Lienar Search 
class Sorting:
    def linearSearch(self,arr,target):
        n = len(arr)-1
        if not arr:
            return 0 
        for i in range(0,n):
            if(arr[i]==target):
                return True
        return False

ans = Sorting()
arr = [4,3,2,5,7,8,4,3]
print(ans.linearSearch(arr,target=7))