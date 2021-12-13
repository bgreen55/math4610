
**Routine Name:**           matrixSubtraction

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 matrixSubtraction.py


**Description/Purpose:** This routine will subtract two matrices of the same size.

**Input:** The input takes two matrices of the same size and containing real numbers.

**Output:** This routine returns a matrix containing real numbers that is the same size as the matrices passed into the routine. 

**Usage/Example:**

The routine takes two arguments.  The arguments are both matrices of the same size. Then each entry in a matrix will be subtracted to the equivalent entry 
in the other matrix, and then the new matrix will be returned.  The order in which the matrices are passed into the routine will effect the output matrix. 
The matrix passed in first, will have the values of the second matrix passed in taken away from it. 


**Implementation/Code:** The following is the code for matirxSubtraction(A, B)

    def matrixSubtraction(A, B):
        m = len(A)
        n = len(A[0][:])
        x = []
        for i in range(m):
            y = [None] * n
            x.append(y)
            for j in range(n):
                x[i][j] = A[i][j] - B[i][j]
        return x
      
      
    main():
        A = [[5, 3], [3, 1], [10, 7]]
        B = [[1, 2], [3, 4], [5, 6]]
        
        print(matrixSubtraction(A, B))
        
        
    main()
    
    
The code above returns the following output:

    [[4, 1], [0, -3], [5, 1]]
    
   

**Last Modified:** December/2021

[Back](../README.md)
