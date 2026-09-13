## Knight Tour Problem 
class backtrack:
    def isValidGrid(self,grid:list[list[int]]) -> bool:
        n = len(grid)
        return self.isValid(grid,0,0,0,n)
     

    def isValid(self,grid:list[list[int]],r:int,c:int,expVal:int,n:int) -> bool:
        if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != expVal:
                return False

        # reached expected moves 
        if expVal == n * n - 1:
                return True

        # All 8 possible knight moves
        ans1 = self.isValid(grid, r - 2, c + 1, expVal + 1, n)
        ans2 = self.isValid(grid, r - 1, c + 2, expVal + 1, n)
        ans3 = self.isValid(grid, r + 1, c + 2, expVal + 1, n)
        ans4 = self.isValid(grid, r + 2, c + 1, expVal + 1, n)
        ans5 = self.isValid(grid, r + 2, c - 1, expVal + 1, n)
        ans6 = self.isValid(grid, r + 1, c - 2, expVal + 1, n)
        ans7 = self.isValid(grid, r - 1, c - 2, expVal + 1, n)
        ans8 = self.isValid(grid, r - 2, c - 1, expVal + 1, n)

        return ans1 or ans2 or ans3 or ans4 or ans5 or ans6 or ans7 or ans8

obj = backtrack()
grid = [
        [0, 7, 6],
        [3, 4, 1],
        [2, 5, 8]
    ]
print(obj.isValidGrid(grid))