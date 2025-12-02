
# Python Data Structures and Best Practices for Level 3 Learners

This repository contains Python programs and activities designed for **A-Level Computer Science** and **Level 3 BTEC Computing** learners. It covers:

- ✅ Arrays (Lists in Python)
- ✅ Stacks (LIFO)
- ✅ Queues (FIFO)
- ✅ Naming Conventions
- ✅ Multi-Dimensional Arrays (Lists and `array` module)

---

## 📚 Learning Objectives
By the end of this repository, learners will:
- Understand **basic and advanced data structures** in Python.
- Implement **Stacks and Queues** using Python lists and `collections.deque`.
- Apply **good naming conventions** for clean, maintainable code.
- Work with **multi-dimensional arrays** using lists and the `array` module.
- Practice coding through **structured activities**.

---

## 1️⃣ Arrays
### **Theory**
An array is a collection of elements stored under one variable name. In Python, arrays are usually implemented using **lists**, which are dynamic and can store mixed data types.

**Key Points:**
- Arrays allow efficient storage and manipulation of data.
- Common operations: `append()`, `remove()`, indexing, iteration.

### **Python Example**
```python
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(30)
print(numbers)
```

### **Why Important?**
Arrays are the foundation for more advanced structures like stacks, queues, and matrices.

---

## 2️⃣ Stacks (LIFO)
### **Theory**
A **stack** is a linear data structure that follows **Last In, First Out (LIFO)**. Think of a stack of plates: the last plate added is the first removed.

### **Operations**
- **Push**: Add an element.
- **Pop**: Remove the last element.

### **Python Example**
```python
# Stack implementation in Python
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
```
### **Why Important?**
Stacks are used in:
 - Undo functionality in applications.
- Function call management in programming.

---

## 3️⃣ Queues (FIFO)
### **Theory**
A **queue** is a linear data structure that follows **First In, First Out (FIFO)**. Think of a line at a shop: the first person in line is served first.

### **Operations**
- **Enqueue**: Add an element to the end of the queue.
- **Dequeue**: Remove the first element from the queue.

### **Python Example**
```python
from collections import deque

# Queue implementation in Python
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
```
### **Why Important?**
Queues are used in:
- Task scheduling.
-Print job management.

---

## 4️⃣ Naming Conventions
### **Theory**
Good naming conventions improve **readability**, **maintainability**, and **collaboration** in programming. Poor naming can lead to confusion and bugs.

### **Best Practices**
- Use **snake_case** for variables and functions (e.g., `student_name`, `calculate_average`).
- Use **PascalCase** for class names (e.g., `StudentRecord`).
- Avoid single-letter names unless in loops (e.g., `i` for iteration).
- Use descriptive names that reflect the purpose of the variable or function.

### **Examples**
```python
# ✅ Good Naming
student_name = "Alice"
def calculate_average(scores):
    return sum(scores) / len(scores)

# ❌ Bad Naming
a = "Alice"
def ca(s):
    return sum(s) / len(s)
```
### **Why Important?**
- Makes code easier to understand for others (and your future self).
- Reduces errors when working in teams.
- Aligns with industry standards for professional development.
---

## 5️⃣ Multi-Dimensional Arrays
### **Theory**
Multi-dimensional arrays store data in rows and columns (like a matrix). They are useful for:
- Representing grids (e.g., game boards).
- Storing tabular data (e.g., spreadsheets).
- Performing mathematical operations (e.g., matrices in linear algebra).

In Python, multi-dimensional arrays can be implemented using:
- **Nested Lists** (lists inside lists).
- **`array` module** (for numeric data types).

---

### **Using Lists**
```python
# Multi-dimensional array using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 1, column 2
print("Element at [1][2]:", matrix[1][2])  # Output: 6

# Iterate through rows and columns
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
```
``` Python
# Using array Module

from array import array

# Multi-dimensional array using array module (nested arrays)
row1 = array('i', [1, 2, 3])
row2 = array('i', [4, 5, 6])
row3 = array('i', [7, 8, 9])

matrix = [row1, row2, row3]

# Access element at row 2, column 1
print("Element at [2][1]:", matrix[2][1])  # Output: 8

# Iterate through matrix
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
```
### **Why Important?**
Multi-dimensional arrays are essential for:
- Image processing.
- Scientific computing.
- Representing complex data structures.

---

