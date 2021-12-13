
**Routine Name:**           prodOfRectMatrices

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 prodOfRectMatrices.py


**Description/Purpose:** This routine will multiply two rectangular matrices together and return a matrix

**Input:** The input is two matrices of size nxm and mxk size.  The entries of the matrices must be real numbers. 

**Output:** This routine returns a matrix of nxk size where the size of matrix A passed in is nxm and the size of matrix B passed in is nxk. The entries of 
the matrix will be all real numbers.

**Usage/Example:**

The routine takes two arguments both being rectangular matrices.  One of the matrices size is nxm and the others is mxk.  The size of the output matrix will be 
nxk. The matrices must be passed into the routine in this order.  If the order is backwards, or the matrices are not compatible to multiply together, an error 
will be returned saying the matrices cannot be multiplied together. 


**Implementation/Code:** The following is the code for prodOfRectMatrices(A, B):


    def prodOfRectMatrices(A, B):
        q = len(A)
        p = len(A[0][:])

        m = len(B)
        n = len(B[0][:])

        try:
            x = []
            for i in range(q):
                y = [None] * n
                x.append(y)

            for i in range(q):   # loops twice
                for j in range(n):    # loops twice
                    x[i][j] = 0
                    for k in range(p):    # loops three times
                        x[i][j] += A[i][k] * B[k][j]

            return x
        except:
            return "The matrices you entered cannot be multiplied together this way"

      
    main():
        C = [
            [1, 2, 3],
            [4, 5, 6]
        ]

        D = [
            [1, 2],
            [5, 6]
        ]
        
        A = [
            [1, 2],
            [5, 6]
        ]
        
        B = [
            [1, 2, 3],
            [4, 5, 6]
        ]

        print(prodOfRectMatrices(C, D))
        print()
        print(prodOfRectMatrices(B, A))
        
        
    main()
    
    
The code above returns the following output:

    [[9, 12, 15], [29, 40, 51]]
    
    The matrices you entered cannot be multiplied together this way

   
The output shows exampes of a matrices that are compatible of being multiplied together, and then switching the order the matrices are multiplied together 
and seeing they no longer can be multiplied together. 

**Last Modified:** December/2021

[Back](../README.md)
