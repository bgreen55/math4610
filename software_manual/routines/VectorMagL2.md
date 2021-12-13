
**Routine Name:**           vectorMagL2

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 vectorMagL2.py


**Description/Purpose:** This routine will find the L2 norm magnitude of a vector.  This is also called the shortest path vector.

**Input:** The input takes a vector containing real numbers.

**Output:** This routine returns a real number. 

**Usage/Example:**

The routine takes a vector as input, squares each of its entries, adds the squares together, then takes the square root.

**Implementation/Code:** The following is the code for vectorMagL2(A)

    import math

    def vectorMagL2(A):
        n = len(A)
        x = 0
        for i in range(n):
            x = x + (A[i] * A[i])
        ans = math.sqrt(x)
        return ans
   
      
    main():
        A = [1, 2, 3]
        print(vectorMagL2(A))
        
        
    main()
    
    
The code above returns the following output:

    3.7416573867739413
    
   

**Last Modified:** December/2021

[Back](../README.md)
