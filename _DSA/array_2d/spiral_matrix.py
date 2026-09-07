# Print spiral matrix in order
class Array_2D:
    def print_spiral(self, matrix: list[list[int]]) -> list[int]:
        if not matrix: # TC:O(m*n)
            return []

        ans = []
        m, n = len(matrix), len(matrix[0])
        srow, erow = 0, m - 1  # top & bottom boundaries
        scol, ecol = 0, n - 1  # left & right boundaries

        while srow <= erow and scol <= ecol:
            # 1. Top row (left to right)
            for j in range(scol, ecol + 1):
                ans.append(matrix[srow][j])

            # 2. Right column (top to bottom)
            for i in range(srow + 1, erow + 1):
                ans.append(matrix[i][ecol])

            # 3. Bottom row (right to left) - check to avoid duplicate row
            if srow < erow:
                for j in range(ecol - 1, scol - 1, -1):
                    ans.append(matrix[erow][j])

            # 4. Left column (bottom to top) - check to avoid duplicate column
            if scol < ecol:
                for i in range(erow - 1, srow, -1):
                    ans.append(matrix[i][scol])

            # Move boundaries inward
            srow += 1
            scol += 1
            erow -= 1 
            ecol -= 1
        return ans


# Example Usage
obj = Array_2D()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(obj.print_spiral(matrix))