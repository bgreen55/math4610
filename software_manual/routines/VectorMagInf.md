
**Routine Name:**           vectorMagInf

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 vectorMagInf.py


**Description/Purpose:** This routine will find the Infinity norm magnitude of a vector.  

**Input:** The input takes a vector containing real numbers.

**Output:** This routine returns a real number. 

**Usage/Example:**

The routine takes a vector as input, finds the entry with the greatest magnitude, and returns the magnitude of that entry.

**Implementation/Code:** The following is the code for vectorMagInf(A)

    def vectorMagInfinity(A):
        n = len(A)
        x = 0
        for i in range(n):
            if abs(A[i]) > x:
                x = abs(A[i])
        return x
   
      
    main():
        A = [1, 2, 3]
        print(vectorMagInf(A))
        
        
    main()
    
    
The code above returns the following output:

    3
    
   

**Last Modified:** December/2021

[Back](../README.md)
