
**Routine Name:**           errorL1

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 errorL1.py


**Description/Purpose:** This routine will find L1 norm error between two vectors

**Input:** The input takes two vectors of same length containing real numbers.

**Output:** This routine returns a real number. 

**Usage/Example:**

The routine takes two vectors as input, sums up the magnitudes of each entry in both vectors, and then returns the magnitude of the difference of those sums 
of vectors.

**Implementation/Code:** The following is the code for errorL1(A, B)

    def errorL1(A, B):
        n = len(A)
        x = 0
        for i in range(n):
            x += abs(A[i]) - abs(B[i])
        return abs(x)
   
      
    main():
        A = [1, 2, 3]
        B = [2, 1, 5]
        print(errorL1(A, B))
        
        
    main()
    
    
The code above returns the following output:

    2
    
   

**Last Modified:** December/2021

[Back](../README.md)
