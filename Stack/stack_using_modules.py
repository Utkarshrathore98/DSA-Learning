# Implementation of Stack using Modules.

# first way using collections.deque()
import collections
stack = collections.deque()

stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()

# second way using queue.LifoQueue
import queue
stack_1 = queue.LifoQueue

# using put for inserting the element same like append
stack_1.put(10)
stack_1.put(20)
stack_1.put(30)

# using get for removing the element same like pop
stack_1.get()
