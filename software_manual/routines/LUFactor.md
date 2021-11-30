
**Routine Name:**           LUfactor

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 LUfactor.py


**Description/Purpose:** This routine uses LU factorization, forward substitution and backwards substitution to solve for x in the linear system Ax=b

**Input:**  The routine needs to be given a square matrix and a vector of the same length as the provided matrix.

**Output:** This routine returns a vector of equal length to the vector given to the routine.

**Usage/Example:**


The code shows the following example.  A matrix called A and a vector called b are passed into the LUfactor routine.  The LU factor routine then 
creates the lower and upper triangular matrices used in LU factorization.  The routine then calls the forwardSub routine and passes the lower tirangular
 matirx L and the vector b to this method.  This creates the vector y.  Then the backSub routine is called and the upper triangular matrix U and the 
 vector y is passed into that method.  That returns the vector x, which is in return returned from the LUfactor routine to solve the linear system 
 Ax = b.



**Implementation/Code:** The following is the code for LUfactor(A, b)



    def LUfactor(A, b):
        n = len(A)

        # create a matrix that is L + U of the matrix A
        for k in range(0, n - 1, 1):
            for i in range(k + 1, n, 1):
                factor = A[i][k] / A[k][k]
                for j in range(k + 1, n, 1):
                    A[i][j] = A[i][j] - factor * A[k][j]
                A[i][k] = factor

        # create lower and upper triangular matrix
        L = []
        U = []
        for i in range(n):
            secondL = []
            secondU = []
            for j in range(n):
                secondL.append(0)
                secondU.append(0)
            L.append(secondL)
            U.append(secondU)

        # give Lower and upper triangular matrices the values they are supposed to have
        for i in range(n):
            for j in range(n):
                if i == j:
                    U[i][j] = A[i][j]
                    L[i][j] = 1
                elif i < j:
                    U[i][j] = A[i][j]
                    L[i][j] = 0
                else:
                    U[i][j] = 0
                    L[i][j] = A[i][j]

        # solve Ly = b for y using forward substitution
        y = forwardSub(L, b)

        # solve Ux = y for x using backwards substitution
        x = backSub(U, y)

        return x



    def forwardSub(A, b):
        n = len(A)
        y = [None] * n
        for i in range(0, n):
            sum = b[i]
            for j in range(0, i):
                sum = sum - (A[i][j] * y[j])
            y[i] = sum / A[i][i]

        return y


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


    def main():
        A = [[1, 1, -1], [1, -2, 3], [2, 3, 1]]
        b = [1, 1, 1]

        x = LUfactor(A, b)
        print(x)


    main()


Running this routine, the following output was returned. 

    
    Solution
    [1.0769230769230769, -0.3076923076923077, -0.23076923076923078]

**Last Modified:** November/2021

[Back](../README.md)
