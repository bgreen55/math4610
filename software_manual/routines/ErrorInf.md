
**Routine Name:**           errorInf

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 errorInf.py


**Description/Purpose:** This routine will find Inf norm error between two vectors

**Input:** The input takes two vectors of same length containing real numbers.

**Output:** This routine returns a real number. 

**Usage/Example:**

The routine takes two vectors as input, finds the entry of greatest magnitude in each vector, and returns the difference in the magnitude of those two. 

**Implementation/Code:** The following is the code for errorInf(A, B)


    def errorInf(A, B):
        n = len(A)
        x = 0
        m = 0
        for i in range(n):
            if abs(A[i]) > x:
                x = abs(A[i])

            if abs(B[i]) > m:
                m = B[i]
        ans = abs(x - m)
        return ans
   
      
    main():
        A = [1, 2, 3]
        B = [2, 1, 5]
        print(errorInf(A, B))
        
        
    main()
    
    
The code above returns the following output:

    2
    
   

**Last Modified:** December/2021

[Back](../README.md)
