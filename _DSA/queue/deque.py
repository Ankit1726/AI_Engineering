## ---------------- Double Ended Queue -----------------
from collections import deque

dq = deque() # TC:O(1)
# insert at front and back
dq.append(2)
dq.append(3)
dq.appendleft(1)
dq.appendleft(4)
print(dq)

dq.pop()
dq.popleft()
print(dq)