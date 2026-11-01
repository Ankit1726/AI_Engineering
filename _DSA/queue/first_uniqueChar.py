## --------------------- First Unique Character --------------------
from collections import deque


class Queue: # TC:O(n) & SC:O(n)
    def first_UniqueChar(self, s: str) -> int:
        freq = {}
        Q = deque()

        for i in range(len(s)):
            char = s[i]

            # Update frequency and push index to queue
            freq[char] = freq.get(char, 0) + 1
            Q.append(i)

            # Pop() repeated item in queue
            while Q and freq[s[Q[0]]] > 1:
                Q.popleft()

        # empty queue --> -1
        return Q[0] if Q else -1


q = Queue()
str = "loveleetcode"
ans = q.first_UniqueChar(str)
print(f"First Unique Character Index: {ans}")