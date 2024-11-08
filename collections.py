stack = []
# Push (add) an element
stack.append(1)
stack.append(2)
stack.append(3)
# Pop (remove) an element
element = stack.pop()  # Removes and returns 3
print(stack) 



from collections import (
    deque
)
queue = deque()
# Enqueue (add) an element
queue.append(1)
queue.append(2)
queue.append(3)
# Dequeue (remove) an element
element = queue.popleft()  # Removes and returns 1
print(queue) 