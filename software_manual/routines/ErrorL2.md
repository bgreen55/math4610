
**Routine Name:**           errorL2

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 errorL2.py


**Description/Purpose:** This routine will find L2 norm error between two vectors

**Input:** The input takes two vectors of same length containing real numbers.

**Output:** This routine returns a real number. 

**Usage/Example:**

The routine takes two vectors as input.  It then finds the difference in magnitude for each n entry in the vectors.  Then the routines sums up the difference 
in magnitudes and returns the square root of that sum.

**Implementation/Code:** The following is the code for errorL2(A, B)

    import math

    def errorL2(A, B):
        n = len(A)
        sum = 0
        for i in range(n):
            diff = A[i] - B[i]
            sum = sum + (diff * diff)
        return math.sqrt(sum)
    
      
    main():
        A = [1, 2, 3]
        B = [2, 1, 5]
        print(errorL1(A, B))
        
        
    main()
    
    
The code above returns the following output:

    2.449489742783178
    
   

**Last Modified:** December/2021

[Back](../README.md)
