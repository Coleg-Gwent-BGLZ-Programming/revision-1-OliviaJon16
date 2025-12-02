"""
Queues in Python - Example and Activity
"""
from collections import deque

# Queue using deque
queue = deque()

# Enqueue elements
queue.append('X')
queue.append('Y')
queue.append('Z')
print("Queue after enqueues:", queue)

# Dequeue element
dequeued = queue.popleft()
print("Dequeued element:", dequeued)
print("Queue after dequeue:", queue)

"""
Activity:
- Create a queue for customer names.
- Add 3 customers and remove 1.
- Print the queue after each operation.
"""
