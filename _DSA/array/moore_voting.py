## Majority Element (Moore Algorithm)
class Array:
    def moore_voting(self, arr):
        freq = 0
        ans = 0
        
        for val in arr:
            if freq == 0:
                ans = val
                freq = 1
            elif ans == val:
                freq += 1
            else:
                freq -= 1  
        return ans

ans = Array()
arr = [1, 2, 2, 1, 1, 3]
print(ans.moore_voting(arr))  # Output: 1