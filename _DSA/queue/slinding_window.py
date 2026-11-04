## --------------------- Sliding Window Maximum -----------------------

from collections import deque


class Queue: # TC:O(n) & SC:O(k)
    def max_sw(self,arr: list[int], k: int) -> list[int]:
        dq = deque()  # store idx
        res = []

        for i in range(len(arr)):
            # remove <-- idx out of curr window front
            if dq and dq[0] <= i - k:
                dq.popleft()

            # remove  <-- back element <= curr
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            # add current idx to back
            dq.append(i)

            # add maximum element of curr --> window ans
            if i >= k - 1:
                res.append(arr[dq[0]])
        return res


sol = Queue()
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sol.max_sw(arr, k))