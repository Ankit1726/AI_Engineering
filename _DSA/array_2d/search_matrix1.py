## Search in 2D matrix Varaiation-1
class Array_2D:
    def searchRow(self, matrix, tar, row):  # TC:O(log(m*n))
        n = len(matrix[0])
        st, end = 0, n - 1
        while st <= end:
            mid = st + (end - st) // 2

            if matrix[row][mid] == tar:
                return True
            elif tar > matrix[row][mid]:
                st = mid + 1
            else:
                end = mid - 1
        return False

    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0]) - 1

        if not m and not n:
            return False

        stRow, endRow = 0, n - 1
        while stRow <= endRow:
            # calculate mid
            midR = stRow + (endRow - stRow) // 2

            if target >= matrix[midR][0] and target <= matrix[midR][n - 1]:
                return self.searchRow(matrix, target, midR)
            elif target >= matrix[midR][n - 1]:
                stRow = midR + 1
            else:
                endRow = midR - 1
        return False


obj = Array_2D()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(obj.searchMatrix(matrix, target=34))