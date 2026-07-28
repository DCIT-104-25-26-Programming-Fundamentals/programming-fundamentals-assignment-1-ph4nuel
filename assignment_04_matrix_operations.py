# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS FOR DISPLAY & INPUT
# -----------------------------------------------------------------------------
def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:4d}", end="")
        print()

def read_matrix(rows):
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ")
        row = [int(x) for x in row_input.split()]
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed

def add_matrices(matrixA, matrixB):
    rows = len(matrixA)
    cols = len(matrixA[0])
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrixA[r][c] + matrixB[r][c])
        result.append(new_row)
    return result

def multiply_matrices(matrixA, matrixB):
    rows_A = len(matrixA)
    cols_A = len(matrixA[0])
    cols_B = len(matrixB[0])
    result = []
    for r in range(rows_A):
        new_row = []
        for c in range(cols_B):
            cell_sum = 0
            for k in range(cols_A):
                cell_sum += matrixA[r][k] * matrixB[k][c]
            new_row.append(cell_sum)
        result.append(new_row)
    return result


M_a = int(input("Enter number of rows: "))
N_a = int(input("Enter number of columns: "))
matrix_part_a = read_matrix(M_a)

print("\nOriginal Matrix:")
print_matrix(matrix_part_a)
print("\nTransposed Matrix:")
print_matrix(transpose_matrix(matrix_part_a))

M_b = int(input("\nEnter number of rows: "))
N_b = int(input("Enter number of columns: "))
matrixA_add = read_matrix(M_b)
matrixB_add = read_matrix(M_b)

print("\nMatrix A:")
print_matrix(matrixA_add)
print("\nMatrix B:")
print_matrix(matrixB_add)
print("\nSum (A + B):")
print_matrix(add_matrices(matrixA_add, matrixB_add))

M_c = int(input("\nEnter number of rows for Matrix A: "))
N_c = int(input("Enter number of columns for Matrix A / rows for Matrix B: "))
P_c = int(input("Enter number of columns for Matrix B: "))
matrixA_mult = read_matrix(M_c)
matrixB_mult = read_matrix(N_c)

print("\nMatrix A:")
print_matrix(matrixA_mult)
print("\nMatrix B:")
print_matrix(matrixB_mult)
print("\nProduct (A x B):")
print_matrix(multiply_matrices(matrixA_mult, matrixB_mult))


