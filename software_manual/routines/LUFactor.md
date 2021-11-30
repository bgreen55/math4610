
**Routine Name:**           LUfactor

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 GEwithBackSub.py


**Description/Purpose:** This routine uses Gaussian elination and back substitution to solve for x in a linear system Ax=b

**Input:**  The routine needs to be given a square matrix and a vector of the same length as the provided matrix.

**Output:** This routine returns a vector of equal length to the vector given to the routine.

**Usage/Example:**


The code shows the following example.  A random square diagonally dominant matrix called A is created that is size 3x3.  An all one vector of 
length 3 is also created called b.  The routine GEwithBackSub then takes the matrix A and vector b as agruments and solves for x in Ax=b.  To 
solve, back substitution is needed, so the method GEwithBackSub calls the all ready created method backSub, to do the back substitution for it. 
A vector x is then returned and printed to the screen 



**Implementation/Code:** The following is the code for GEwithBackSub(A, b)

    

    from random import randint


    def GEwithBackSub(A, b):
        n = len(b)

        # gaussian elimination
        for k in range(0, n, 1):
            for i in range(k + 1, n, 1):
                factor = A[i][k] / A[k][k]
                for j in range(k, n, 1):
                    A[i][j] = A[i][j] - factor * A[k][j]
                b[i] = b[i] - factor * b[k]


        x = backSub(A, b)

        return x


    def diagDomMatrix(n):
        A = []

        for i in range(n):
            x = []
            for j in range(n):
                if j == i:
                    value = randint(0, 8)
                    x.append(value)
                else:
                    value = randint(0, 8)
                    x.append(value)

            A.append(x)

        # make the diagonal entry of the matrix greater than the sum of the other entries in the row
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum = sum + A[i][j]

            if A[i][i] <= sum:
                value = randint(sum, sum + 10)
                A[i][i] = value

        for i in range(n):
            for j in range(n):
                print(A[i][j], end=" ")
            print()
        print()
        # returning the matrix A allows it to be used by other funcitons
        return A


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
        # random daigonal dominant martix of size 3x3
        print("The random diagonal dominant matrix")
        A = diagDomMatrix(3)
        # b vector size 1x3
        print("The column vector b")
        b = [1, 1, 1]
        print(b)

        print("\nSolution")
        x = GEwbackSub(A, b)
        print(x)


    main()


Running this routine, the following output was one of the possible outputs that was returned. 

    The random diagonally dominant matrix
    4 1 2
    7 12 4
    3 7 15
    
    The column vector b 
    1 1 1
    
    Solution
    0.24214417744916822, -0.07578558225508318, 0.053604436229205174

**Last Modified:** November/2021

[Back](../README.md)
