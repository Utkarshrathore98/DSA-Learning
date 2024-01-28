# first way using collections.deque()

import collections
q = collections.deque()

# insertion from left of queue.
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)

# deletion from right of queue.
q.pop()

# insertion from right of queue.
q.append(40)
q.append(50)
q.append(60)

# deletion from left of queue.
q.popleft()

# check if queue is empty or not.
not q

# second way using queue.Queue()
import queue
q = queue.Queue()

# insertion of element in queue
q.put(10)
q.put(20)
q.put(30)

# removal of element from queue
q.get()