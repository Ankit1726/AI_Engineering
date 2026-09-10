## find missing and repated values 
class Array_2D: # TC:O(n^2)
    def find_missing(self,grid:list[list[int]]) -> list[int]:
        n = len(grid)
        s = set()
        actual_sum = 0 
        a = -1 # reapted value 

        for i in range(n):
            for j in range(n):
                val = grid[i][j] # (i,j) cell 
                actual_sum+=val

                if val in s:
                    a = val # add repated number 
                s.add(val)

        total_nums = n*n 
        exp_sum = (total_nums * (total_nums+1))//2 

        # calculate missing number
        b = exp_sum + a - actual_sum 
        return [a,b]

obj = Array_2D()
grid = [[9,1,7],
       [8,9,2],
       [3,4,6]]
ans = obj.find_missing(grid)
print(ans)