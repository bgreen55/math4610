
**Routine Name:**           vectorMagL1

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 vectorMagL1.py


**Description/Purpose:** This routine will find the L1 norm magnitude of a vector.  This is also sometimes called the city block magnitude

**Input:** The input takes a vector containing real numbers.

**Output:** This routine returns a real number. 

**Usage/Example:**

The routine takes a vector as input, sums up each entry in the vector, and returns the sum.

**Implementation/Code:** The following is the code for vectorMagL1(A)

    def vectorMagL1(A):
        n = len(A)
        x = 0
        for i in range(n):
            x += abs(A[i])
        return x
   
      
    main():
        A = [1, 2, 3]
        
        print(vectorMagL1(A, B))
        
        
    main()
    
    
The code above returns the following output:

    6
    
   

**Last Modified:** December/2021

[Back](../README.md)
