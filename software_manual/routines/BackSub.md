
**Routine Name:**          BackSub

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 BackSub.py


**Description/Purpose:** This routine implements back substitution to solve for x in a linear system Ax=b when A is in upper triangular form.

**Input:**  The routine needs to be given a square matrix in upper triangular form that is filled with real numbers.  
The routine also takes vector of the same length as the provided matrix that contains only real numbers.

**Output:** This routine returns a vector of real numbers that is equal length to the vector given to the routine.

**Usage/Example:**


The code shows the following example.  An upper trianglar matrix is initialized with size 3 by the function that creates a singular upper 
triangular matrix for each size. It also returns a vector of ones that is the same length as the matrix.  The matrix and the vector are passed 
into the method backSub(A, b), and the solution vector of the linear system is returned from the method and printed to the screen.



**Implementation/Code:** The following is the code for backSub(A, b)


   
    # this function preforms back substitution on an upper triangular matrix to solve for x in Ax=b
    def backSub(A, b):
        n = len(b)
        x = [None] * n

        m = n - 1
        x[m] = b[m] / A[m][m]
        for i in range(m - 1, -1, -1):
            sum = b[i]
            for j in range(i + 1, n, 1):
                sum = sum - A[i][j] * x[j]
            x[i] = sum / A[i][i]

        return x
        
        
    # this function initializes an upper triangular matrix
    def matrixInit(n):
        matrixA = []
        matrixb = []

        for i in range(n):
            a = []
            for j in range(n):
                if j < i:
                    a.append(0)
                else:
                    a.append(i + j - 1)
            matrixA.append(a)

        for i in range(n):
            matrixb.append(1)

        return matrixA, matrixb


    def main():
        print("Task 1\n")
        # get matrix A of size nxn and a nx1 vector b of all 1
        A, b = matrixInit(3)
        # preform backsubstitution on on A to solve for x in Ax = b
        solution = backSub(A, b)
        print(solution)


    main()



Running this routine, the following output was returned. 

    [-0.6666666666666667, 0.33333333333333337, 0.3333333333333333]

**Last Modified:** November/2021

[Back](../README.md)
