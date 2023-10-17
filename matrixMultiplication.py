import numpy as np

# Input the dimensions of matrices A, B, and C
m = int(input("Enter the number of rows for matrix A: "))
n = int(input("Enter the number of columns for matrix A and rows for matrix B: "))
r = int(input("Enter the number of columns for matrix B: "))

#declaring matrix 
A = np.empty((m, n))
B = np.empty((n, r))
C = np.empty((m, r))

#input values for A
for i in range(m):
    for j in range(n):
        z = int(input(f"Enter value for A[{i}][{j}]: "))
        A[i][j] = z

#input values for B
for i in range(n):
    for j in range(r):
        z = int(input(f"Enter value for B[{i}][{j}]: "))
        B[i][j] = z

# matrix multiplication
for i in range(m):
    for j in range(r):
        # Initialize the value in C to 0
        C[i][j] = 0
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

# result matrix C
for i in range(m):
    for j in range(r):
        print(C[i][j])
