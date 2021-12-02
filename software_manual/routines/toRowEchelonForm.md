
**Routine Name:**          toRowEchelonForm

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 toRowEchelonForm.py


**Description/Purpose:** This routine implements takes a given matrix and vector, A and b in a system Ax=b, and does transformations to put both the 
matrix and vector in row echelon form.

**Input:**  The routine needs to be given a square matrix that contains real numbers of size nxn.  The routine also takes a vector of size 1xn that also 
only contains real numbers.

**Output:** This routine returns the matrix A and the vector b in there own arrays after they have been transformed into row echelon form. 

**Usage/Example:**

The code shows the following example. A random matrix of size 3x3 is generated. That matrix and a 3x1 vector of all ones is passed into the 
toRowEchelonForm routine.  That routine then returns both the matrix and the vector when they have both been reduced to row echelon form.  
The code the prints the matrix and the vector.



**Implementation/Code:** The following is the code for toRowEchelonForm(A, b)

        
    # this method takes a square matrix A and puts it into row echelon form
    def toRowEchelonForm(A, b):
        n = len(b)
        s = [None] * n

        for i in range(0, n, 1):
            s[i] = abs(A[i][0])
            for j in range(0, n, 1):
                temp1 = abs(A[i][j])
                if temp1 > s[i]:
                    s[i] = temp1

        for k in range(0, n -1, 1):
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

            for j in range(0, n , 1):
                temp1 = A[k][j]
                A[k][j] = A[q][j]
                A[q][j] = temp1

            for i in range(k+1, n, 1):
                factor = A[i][k] / A[k][k]
                for j in range(k, n, 1):
                    A[i][j] = A[i][j] - factor * A[k][j]
                b[i] = b[i] - factor * b[k]

        return A, b    
        
    
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

        return A


    def main():
        # create a random square matrix
        A = randSqrMatrix(3)

        b = [1, 4, 5]

        # do transformations on A and b to put A in upper row echelon form
        result1, result2 = toRowEchelonForm(A, b)

        print(result1)
        print()
        print(result2)


    main()



Running this routine, the following output is one of the possible outputs that could returned. 

    [[7, 4, 2], [0.0, 3.0, 0.0], [0.0, 0.0, 8.0]]

    [1, 5.0, 6.333333333333333]
    
The first array is the matrix A in row echelon form and the second array is the vector in row echelon form. 
    

**Last Modified:** November/2021

[Back](../README.md)
