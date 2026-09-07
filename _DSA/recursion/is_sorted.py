## check array is-sorted usingrecursion 
class recursion:
    def is_sorted(self, arr, n=None): # TC:O(n) & SC:O(n)
        if n is None:
            n = len(arr)
        if n <= 1:
            return True
        
        check = arr[n - 1] >= arr[n - 2]
        return check and self.is_sorted(arr, n - 1)

obj = recursion()
arr = [1,2,7,4,5]
print(obj.is_sorted(arr))