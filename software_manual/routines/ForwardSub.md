
**Routine Name:**          ForwardSub

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 ForwardSub.py


**Description/Purpose:** This routine implements forward substitution to solve for x in a linear system Ax=b when A is in lower triangular form.

**Input:**  The routine needs to be given a square matrix in lower triangular form that is filled with real numbers.  
The routine also takes vector of the same length as the provided matrix that contains only real numbers.

**Output:** This routine returns a vector of real numbers that is equal length to the vector given to the routine.

**Usage/Example:**


The code shows the following example.  An upper trianglar matrix is initialized with size 4 by the function that creates a singular upper 
triangular matrix for each size. It also returns a vector of ones that is the same length as the matrix.  The upper triangular matrix is then 
transposed using the transposeMatrix(A) method, which makes the matrix now in lower triangular form.  The matrix and the vector are passed 
into the method forwardSub(A, b), and the solution vector of the linear system is returned from the method and printed to the screen.



**Implementation/Code:** The following is the code for forwardub(A, b)

        
    # this function takes A and b in Ax = b and returns x.  The fucntion preforms forwards substitution to solve lower triangular matrix
    def forwardSub(A, b):
        n = len(A)
        y = [None] * n

        for i in range(0, n):
            sum = b[i]
            for j in range(0, i):
                sum = sum - (A[i][j] * y[j])

            y[i] = sum / A[i][i]

        return y

    
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


    # this function transposes a matrix
    def transposeMatrix(A):
        n = len(A)
        x = []

        # create empty transposed matrix as x
        for i in range(n):
            a = []
            for j in range(n):
                a.append(None)
            x.append(a)

        # take values from A and put them in the transposed matrix
        for i in range(n):
            for j in range(n):
                x[j][i] = A[i][j]

        return x
        

    def main():
        print("Task 2")
        A, b = task1.matrixInit(4)

        x = transposeMatrix(A)
        y = forwardSub(x, b)

        print(y)


    main()



Running this routine, the following output was returned. 

    [-1.0, 1.0, 0.0, 0.0]

**Last Modified:** November/2021

[Back](../README.md)
