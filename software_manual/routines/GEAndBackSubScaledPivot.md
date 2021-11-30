
**Routine Name:**           GEAndBackSubScaledPivot 

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 GEAndBackSubScaledPivot.py


**Description/Purpose:** This routine uses Gaussian Elimination and the method of scaled partial pivoting to solve for x in the linear system Ax=b when 
given A and b

**Input:**  The routine needs to be given a square matrix and a vector of the same length as the provided matrix.

**Output:** This routine returns a vector of equal length to the vector given to the routine.

**Usage/Example:**


The code shows the following example.  Given a matrix A and a vector b, the routine uses the method of scaled partial pivoting to transform the matrix A 
into upper echelon form, before preforming back substitution to solve for the vector x of the linear system Ax=b.  As long as the scalers are kept non-zero 
the linear equation will be solved without running into issues.  The issues that may arries are dividing by zero. 



**Implementation/Code:** The following is the code for GEAndBackSubScaledPivot(A, b)


    def GEAndBackSubScaledPivot(A, b):
        # Ax = b is the matrix form
        n = len(b)
        s = [None] * n

        # gaussian elimination
        for i in range(0, n, 1):
            s[i] = abs(A[i][0])
            for j in range(0, n, 1):
                temp1 = abs(A[i][j])
                if temp1 > s[i]:
                    s[i] = temp1

        for k in range(0, n - 1, 1):
            temp1 = abs(A[k][k] / s[k])
            q = k
            for i in range(k + 1, n, 1):
                temp2 = abs(A[i][k] / s[i])
                if temp1 < temp2:
                    temp1 = temp2
                    q = i

            temp1 = b[k]
            b[k] = b[q]
            b[q] = temp1
            temp1 = s[k]
            s[k] = s[q]
            s[q] = temp1

            for j in range(0, n, 1):
                temp1 = A[k][j]
                A[k][j] = A[q][j]
                A[q][j] = temp1

            for i in range(k + 1, n, 1):
                factor = A[i][k] / A[k][k]
                for j in range(k, n, 1):
                    A[i][j] = A[i][j] - factor * A[k][j]
                b[i] = b[i] - factor * b[k]

        # back substitution
        length = len(b)
        x = [None] * length

        m = length - 1
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

        x = GEAndBackSubScaledPivot(A, b)
        print(x)



    main()


Running this routine, the following output was returned. 

    
    Solution
    [1.0769230769230769, -0.3076923076923077, -0.23076923076923078]

**Last Modified:** November/2021

[Back](../README.md)
