"""
Arrays in Python - Example and Activity
"""
# Example: Working with arrays (lists in Python)
numbers = [10, 20, 30, 40, 50]

# Access elements
print("First element:", numbers[0])

# Add an element
numbers.append(60)
print("After append:", numbers)

# Remove an element
numbers.remove(30)
print("After remove:", numbers)

# Iterate through array
for num in numbers:
    print(num)

"""
Activity:
- Create an array of 5 student names.
- Add a new name and remove one.
- Print all names in reverse order.
"""

"""
Stacks in Python - Example and Activity
"""
# Stack using Python list
stack = []

# Push elements
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes:", stack)

# Pop element
popped = stack.pop()
print("Popped element:", popped)
print("Stack after pop:", stack)

"""
Activity:
- Implement a stack that stores integers.
- Push 5 numbers and pop 2.
- Print the remaining stack.
"""

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

"""
Naming Conventions in Python - Example and Activity
"""
# Good naming conventions
student_name = "Alice"  # descriptive variable name
def calculate_average(scores):  # descriptive function name
    return sum(scores) / len(scores)

# Bad naming conventions
a = "Alice"  # unclear variable name
def ca(s):  # unclear function name
    return sum(s) / len(s)

"""
Activity:
- Rewrite a poorly named program using proper naming conventions.
"""

"""
Final Challenge:
Combine arrays, stacks, and queues:
- Store student names in an array.
- Use a stack for undo operations.
- Use a queue for processing tasks.
"""
