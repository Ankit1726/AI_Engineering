## Find Diagonal Sum of Matrix
class Array_2D:
    def diagonal_sum(self, matrix):# TC:(R * C)
        rows = len(matrix)
        cols = len(matrix[0])

        if not rows or not cols:
            return 

        diag_sum = 0
        for i in range(rows):
            for j in range(cols):
                if i == j or j == cols - i - 1:
                    diag_sum += matrix[i][j]
        return diag_sum
    
    def optimised_diagSum(self,matrix): # TC:O(n)
        if not matrix or not matrix[0]:
            return 0 

        n = len(matrix)
        diag_sum = 0 
        for i in range(n):
            # primary diagonal 
            diag_sum+=matrix[i][i]

            # secondary diagonal element 
            if i!=n-i-1:
                diag_sum+=matrix[i][n - i - 1]
        return diag_sum
            
ans = Array_2D()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal = ans.optimised_diagSum(matrix)
print(f"Diagonal Sum:{diagonal}")