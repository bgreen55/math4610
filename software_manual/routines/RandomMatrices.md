
**Routine Name:**          RandomMatrices

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 main.py


**Description/Purpose:** This routine has four methods that create different random matrices of a given size.  Random square, lower, upper and diagonally 
dominant matrices are the matrices that can be created from the methods in the routine. 

**Input:**  Each method needs to be given an integer to create its random matrix.  

**Output:** This routine returns random matrices of real numbers that are nxn size, where n is a positive integer passed into the methods.

**Usage/Example:**

The code shows the following example.  A random square matrix, a matrix in upper triangular form with random entries, a matrix in lower triangular 
form with random entries, and a diagonally dominant matrix with random entries are all created with size 3x3.  This size was chosen for the example 
but can be changed in the method parameters.  The four random matrices are then printed to the screen.  



**Implementation/Code:** The following is the code for forwardub(A, b)

        
    from random import randint

    # this function creates a square matrix of size n with random numbers from 0-10
    def randSqrMatrix(n):
        A = []

        for i in range(n):
            x = []
            for j in range(n):
                value = randint(0, 10)
                x.append(value)
            A.append(x)

        #print the matrix
        for i in range(n):
            for j in range(n):
                print(A[i][j], end=" ")
            print()
        print()

        #return A


    def randUpperTMatrix(n):
        A = []

        for i in range(n):
            x = []
            for j in range(n):
                if j > i:
                    value = randint(0, 10)
                    x.append(value)
                elif j == i:
                    value = randint(1, 10)
                    x.append(value)
                else:
                    x.append(0)
            A.append(x)

        # print the matrix
        for i in range(n):
            for j in range(n):
                print(A[i][j], end=" ")
            print()
        print()


    def randLowerTMatrix(n):
        A = []

        for i in range(n):
            x = []
            for j in range(n):
                if j < i:
                    value = randint(0, 10)
                    x.append(value)
                elif j == i:
                    value = randint(1, 10)
                    x.append(value)
                else:
                    x.append(0)
            A.append(x)

        # print the matrix
        for i in range(n):
            for j in range(n):
                print(A[i][j], end=" ")
            print()
        print()


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

        # returning the matrix A allows it to be used by other funcitons
        #return A
        # print the matrix
        for i in range(n):
            for j in range(n):
                print(A[i][j], end=" ")
            print()
        print()



    def main():
        randSqrMatrix(3)
        randUpperTMatrix(4)
        randLowerTMatrix(4)
        diagDomMatrix(3)

    main()



Running this routine, one of the outputs that could be returned is given below.

    0 3 7 
    2 10 6 
    2 8 2 

    5 9 5 
    0 2 3 
    0 0 4 

    2 0 0 
    1 5 0 
    3 2 2 

    17 4 3 
    4 13 2 
    7 3 17 


**Last Modified:** November/2021

[Back](../README.md)
