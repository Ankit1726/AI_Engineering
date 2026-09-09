# N Queen Problem
import time

class Backtrack:
    def is_safe(self, board, row, col, n):
        # 1. Horizontal Check
        for j in range(n):
            if board[row][j] == "Q":
                return False

        # 2. Vertical Check
        for i in range(n):
            if board[i][col] == "Q":
                return False

        # 3. Upper-Left Diagonal Check
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # 4. Upper-Right Diagonal Check
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def print_board(self, board, n):
        """N-Queens Board ko Grid Format mein print karne ka function"""
        border = "+" + "---+" * n
        print(border)
        for row in board:
            line = "| " + " | ".join(row) + " |"
            print(line)
            print(border)
        print()

    def nQueens(self, n, visualize=False):
        board = [["." for _ in range(n)] for _ in range(n)]
        solutions = []

        def n_queens(row):
            if row == n:
                solutions.append(["".join(r) for r in board])
                print(f"=== SOLUTION FOUND (#{len(solutions)}) ===")
                self.print_board(board, n)
                return

            for col in range(n):
                if self.is_safe(board, row, col, n):
                    board[row][col] = "Q"  # Place Queen

                    if visualize:
                        print(f"Placing Queen at Row {row}, Col {col}:")
                        self.print_board(board, n)
                        time.sleep(0.2)

                    n_queens(row + 1)  # Recursive Call

                    board[row][col] = "."

                    if visualize:
                        print(f"Backtracking from Row {row}, Col {col}:")
                        self.print_board(board, n)

        n_queens(0)
        return solutions


# Execution
obj = Backtrack()
N = 4
print(f"Finding all solutions for N = {N}:\n")
obj.nQueens(N, visualize=False)