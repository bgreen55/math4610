
**Routine Name:**           transposeMatrix

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 transposeMatrix.py


**Description/Purpose:** This routine will transpose a matrix of real numbers. 

**Input:** The input is a matrix of size mxn containing real numbers. 

**Output:** This routine returns a matrix containing real numbers that is of size nxm

**Usage/Example:**

The routine takes one argument, a matrix.  The routine then transposes the matrix and returns the transpose of the matrix.  


**Implementation/Code:** The following is the code for transposeMatrix(A):

    def transposeMatrix(A):
        n = len(A)     
        m = len(A[0][:])     
        x = []
        # create empty transposed matrix as x
        for i in range(m):
            a = []
            for j in range(n):
                a.append(None)
            x.append(a)
        # take values from A and put them in the transposed matrix
        for i in range(m):
            for j in range(n):
                x[i][j] = A[j][i]

        return x
      
      
    main():
        A = [[1, 2, 3], [3, 4, 5]]
        B = [[1, 2], [3, 4], [5, 6]]
        c = [[1, 2], [5, 6]]
        
        print(scalarMultMatrix(A))
        print(transposeMatrix(B))
        print(transposeMatrix(C))
        
        
    main()
    
    
The code above returns the following output:

    [[1, 3], [2, 4], [3, 5]]
    [[1, 3, 5], [2, 4, 6]]
    [[1, 5], [2, 6]]
   
The output shows exampes of a transposed matrix for a mxn matrix, nxm matrix and nxn matrix.

**Last Modified:** December/2021

[Back](../README.md)
