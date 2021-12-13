
**Routine Name:**           dotProduct

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 dotProduct.py


**Description/Purpose:** This routine will sum the multiplications of each entry of two vectors.

**Input:** The input takes two vectors of the same lenght and containing real numbers.

**Output:** This routine returns a real number 

**Usage/Example:**

The routine takes two arguments.  The arguments are both vectors of the same length.  Then each entry in a vector will be multiplied to the equivalent entry 
in the other vector, and then they will be all summed together into one number which the routine will return.


**Implementation/Code:** The following is the code for dotProduct(A, B)

    def dotProduct(A, B):
        n = len(A)
        x = 0
        for i in range(n):
            x += A[i] * B[i]
        return x
      
      
    main():
        A = [1, 2, 3]
        B = [3, 4, 5]
        
        print(dotProduct(A, B))
        
        
    main()
    
    
The code above returns the following output:

    26
    
   

**Last Modified:** December/2021

[Back](../README.md)
