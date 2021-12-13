
**Routine Name:**           sacalarMultMatrix

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 scalarMultMatrix.py


**Description/Purpose:** This routine will multiply a scalar to a matrix of real numbers. 

**Input:** The input a real number as a scalar, and a matrix containing real numbers.  When passing them into the routine, the scalar must go first and the 
matrix must go second. 

**Output:** This routine returns a matrix containing real numbers that is the same size as the matrices passed into the routine. 

**Usage/Example:**

The routine takes two arguments.  The first argument is the scalar and must be a real number. The second argument is a matrix which will have each entry mulitplied 
by the scalar before the matrix is returned. 


**Implementation/Code:** The following is the code for scalarmultMatrix(a, B):

    def scalarMultMatrix(a, B):
        n = len(B)
        m = len(B[0][:])
        x = []
        for i in range(n):
            y = [None] * m
            x.append(y)
            for j in range(m):
                x[i][j] = a * B[i][j]
        return x
      
      
    main():
        a = 3
        B = [[1, 2], [3, 4], [5, 6]]
        
        print(scalarMultMatrix(a, B))
        
        
    main()
    
    
The code above returns the following output:

    [[3, 6], [9, 12], [15, 18]]
    
   

**Last Modified:** December/2021

[Back](../README.md)
