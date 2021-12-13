
**Routine Name:**           rectMatrixMultVect

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 rectMatrixMultVect.py


**Description/Purpose:** This routine will multiply a vector to a rectangular matrix and return a vector. 

**Input:** The input is a vector of either size m or n, and then a matrix of size mxn.

**Output:** This routine returns a vector of real numbers that is either of size m or size n.  The vector will not be the size of the vector passed into the 
routine but will instead be the size of the length of the matrix that is not equal to the length of the multiplying vector.  If the multiplying vector is not 
the size of either lengths of the matrices an error message will be returned. 

**Usage/Example:**

The routine takes two arguments, first a vector and second a rectangular matrix.  Depending on the length of the vector it will either be multiplied to the 
matrix infront of the matrix, or it will be multiplied to the matrix after the matrix. ex: xA or Ax where A is the matix and x is the vector.  


**Implementation/Code:** The following is the code for rectMatrixMultVector(a, B):


    def rectMatrixMultVect(a, B):
        q = len(a)
        # lengths of mxn matrix B
        m = len(B)
        n = len(B[0][:])

        # vector multiplied before the matrix
        if q == m:
            x = [None] * n
            for i in range(n):
                x[i] = 0
                for j in range(m):
                    x[i] += a[j] * B[j][i]
            return x
        # vector multiplied after the matrix
        elif q == n:
            x = [None] * m
            for i in range(m):
                x[i] = 0
                for j in range(n):
                    x[i] += a[j] * B[i][j]
            return x
        else:
            return "The vector is not the same size as either length of the matrix"

      
      
    main():
        t = [1, 2, 3]

        y = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        
        a = [1, 3]
        
        b = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]

        print(rectMatrixMultVect(t, y))
        print()
        print(rectMatrixMultVect(a, b))

        
    main()
    
    
The code above returns the following output:

    [22, 28]
    
    [7, 15, 23]
   
The output shows exampes of a matrix of size mxn being mutiplied by a vector of size n and a vector of size m

**Last Modified:** December/2021

[Back](../README.md)
