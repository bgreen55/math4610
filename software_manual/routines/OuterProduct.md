
**Routine Name:**           outerProduct

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 outerProduct.py


**Description/Purpose:** This routine will multiply a vector of length n and vector of length m together to create an n x m matrix.

**Input:** The input takes two vectors of equal or differing length that contain only real numbers. 

**Output:** This routine returns a matrix of size nxm.

**Usage/Example:**

The routine takes two arguments.  The arguments are both vectors of the same or different length.  The first entry in the first vector will be multiplied by each 
n entry in the second vector.  Each result will become the [1][n] entry in the new matrix.


**Implementation/Code:** The following is the code for outerProduct(A, B)

    def outerProduct(A, B):
        n = len(A)
        m = len(B)
        x = []
        for i in range(n):
            y = [None] * m
            x.append(y)
            for j in range(m):
                x[i][j] = A[i] * B[j]
        return x
      
      
    main():
        A = [1, 2, 3]
        B = [4, 5, 6]
        
        print(outerProduct(A, B))
        
        
    main()
    
    
The code above returns the following output:

    [
     [4, 5, 6],
     [8, 10, 12],
     [12, 15, 18]
     ]
    
   

**Last Modified:** December/2021

[Back](../README.md)
