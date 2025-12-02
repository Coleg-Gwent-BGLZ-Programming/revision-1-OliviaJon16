from array import array

# Multi-Dimensional Arrays using array module (nested arrays)
row1 = array('i', [1, 2, 3])
row2 = array('i', [4, 5, 6])
row3 = array('i', [7, 8, 9])

matrix = [row1, row2, row3]

# Access element at row 2, column 1
print("Element at [2][1]:", matrix[2][1])  # Output: 8

# Iterate through matrix
print("
Matrix elements:")
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()

# Activity:
# 1. Create a 2D array using array module.
# 2. Calculate the sum of all elements.
# 3. Print the diagonal sum.
