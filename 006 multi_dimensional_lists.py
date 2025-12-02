# Multi-Dimensional Arrays using Lists
# Example: 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 1, column 2
print("Element at [1][2]:", matrix[1][2])  # Output: 6

# Iterate through rows and columns
print("
Matrix elements:")
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()

# Activity:
# 1. Create a 3x3 matrix with your own numbers.
# 2. Print the sum of each row.
# 3. Print the diagonal elements.
