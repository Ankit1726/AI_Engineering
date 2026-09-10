## find duplicates in an array 
class array: # TC:O(n) & SC:O(1)
    def findDuplicates(self,arr:list[int]) -> int:
        # Detect Cycle 
        slow = arr[0]
        fast = arr[0]

        while True:
            slow = arr[slow] # +1 
            fast = arr[arr[fast]] # +2 
            if slow == fast:
                break # found cycle

        # find cycle entry point  
        slow = arr[0]
        while slow!=fast:
            slow = arr[slow]
            fast = arr[fast]
        return slow
    
obj = array()
arr = [1, 3, 4, 2, 2]
print(obj.findDuplicates(arr))