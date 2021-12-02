
**Routine Name:**          randDiagMatrix

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 randDiagMatrix.py


**Description/Purpose:** This routine creates a random diagonal matrix of a user given size.

**Input:**  The routine needs to be a real number.

**Output:** This routine returns a matrix of size nxn where n is specified by the user.  The matrix has zero's in every entry but the diagonal, which has 
random whole numbers.

**Usage/Example:**


The code shows the following example.  The method is given the size one wants the matrix to be, then the code outputs a random diagonal matrix of that size. 


**Implementation/Code:** The following is the code for randDiagMatrix(n)

    from random import randint


    def randDiagMatrix(n):
        A = []

        for i in range(n):
            x = []
            for j in range(n):
                if i == j:
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


    def main():
        randDiagMatrix(4)


    main()


Running this routine, the following output is one of the possible outputs that could be returned. 

    1 0 0 0 
    0 3 0 0 
    0 0 3 0 
    0 0 0 4 

**Last Modified:** November/2021

[Back](../README.md)
