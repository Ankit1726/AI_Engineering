## Sort Colors(Dutch national flag)
class Two_Pointer:
    def sort_colors(self, arr):
        left, right = 0, len(arr) - 1
        i = 0
        
        # Loop until i passes the right boundary
        while i <= right:
            if arr[i] == 0:
                # Swap current element with the left boundary
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
                i += 1
            elif arr[i] == 1:
                # Move to the next element
                i += 1
            else: 
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
                
        return arr

ans = Two_Pointer()
arr = [2, 0, 2, 1, 1, 0]
print(ans.sort_colors(arr)) 