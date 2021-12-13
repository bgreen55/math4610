
**Routine Name:**           matrixAddition

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 matrixAddition.py


**Description/Purpose:** This routine will add two matrices of the same size together

**Input:** The input takes two matrices of the same size and containing real numbers.

**Output:** This routine returns a matrix containing real numbers that is the same size as the matrices passed into the routine. 

**Usage/Example:**

The routine takes two arguments.  The arguments are both matrices of the same size. Then each entry in a matrix will be added to the equivalent entry 
in the other matrix, and then the new matrix will be returned.


**Implementation/Code:** The following is the code for matirxAddition(A, B)

    def matrixAddition(A, B):
        m = len(A)
        n = len(A[0][:])
        x = []
        for i in range(m):
            y = [None] * n
            x.append(y)
            for j in range(n):
                x[i][j] = A[i][j] + B[i][j]

        return x
      
      
    main():
        A = [[1, 2], [3, 4], [5, 6]]
        B = [[1, 2], [3, 4], [5, 6]]
        
        print(matrixAddition(A, B))
        
        
    main()
    
    
The code above returns the following output:

    [[2, 4], [6, 8], [10, 12]]
    
   

**Last Modified:** December/2021

[Back](../README.md)
