## Book Allocation Problem
class Sorting:

    @staticmethod # C:O(log(range)*m)
    def isValid(arr: list[int], n: int, m: int, allowedPages: int) -> bool:
        student = 1
        pages = 0
        for i in range(n):
            if arr[i] > allowedPages:
                return False

            if pages + arr[i] <= allowedPages:
                pages += arr[i]
            else:
                student += 1
                pages = arr[i]  # allocate to next student
        return student <= m

    def book_allocation(self, arr: list[int], n: int, m: int) -> int:
        if m > n:
            return -1

        st = max(arr)  # Minimum possible answer is the largest single book
        end = sum(arr)  # Maximum possible answer is reading all books
        ans = -1

        while st <= end:
            mid = st + (end - st) // 2

            if self.isValid(arr, n, m, mid):
                ans = mid
                end = mid - 1  # Try for a smaller maximum
            else:
                st = mid + 1  # Increase allowed max pages

        return ans


res = Sorting()
arr = [2, 1, 3, 4]
n, m = 4, 2
print(res.book_allocation(arr, n, m))  # Output: 6