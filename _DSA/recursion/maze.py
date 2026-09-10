## Rate in maze problem 
class backtracking:
    def helper(self, matrix, r, c, n, ans, path):# TC:O(4^(n^2))
        if r < 0 or c < 0 or r >= n or c >= n or matrix[r][c] <= 0:
            return

        # Destination reached 
        if r == n - 1 and c == n - 1:
            ans.append(path)
            return

        matrix[r][c] = -1  # Mark visited

        # Recursive Calls for 4 Directions
        self.helper(matrix, r + 1, c, n, ans, path + "D")  # Down
        self.helper(matrix, r - 1, c, n, ans, path + "U")  # Up
        self.helper(matrix, r, c - 1, n, ans, path + "L")  # Left
        self.helper(matrix, r, c + 1, n, ans, path + "R")  # Right

        # Backtrack step
        matrix[r][c] = 1  # Unvisited

    def rat_maze(self, matrix):
        n = len(matrix)
        ans = []

        # Base case (start or destination blocked)
        if matrix[0][0] == 0 or matrix[n - 1][n - 1] == 0:
            return ans 
        self.helper(matrix, 0, 0, n, ans, "")
        return ans

# Test
obj = backtracking()
matrix = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

print(obj.rat_maze(matrix))
# Output: ['DDRDRR', 'DRDDRR']