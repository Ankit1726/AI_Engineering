## Merge 2 Sorted Array
class Array:
    def merge_2Sorted(self, A, B, m, n):  # TC:O(m+n) SC:O(1)
        idx = m + n - 1
        i = m - 1
        j = n - 1

        # Compare from back and place larger element at idx
        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[idx] = A[i]
                i -= 1
            else:
                A[idx] = B[j]
                j -= 1
            idx -= 1

        # Copy remaining elements of B (if any)
        while j >= 0:
            A[idx] = B[j]
            j -= 1
            idx -= 1


ans = Array()
A = [1, 2, 3, 0, 0, 0]
B = [2, 5, 6]
m, n = 3, 3

ans.merge_2Sorted(A, B, m, n)
print(A)