
**Routine Name:**           vectorAdd

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 vectorAdd.py


**Description/Purpose:** This routine will add two vectors of the same length together.

**Input:** The input takes two vectors of the same length, both containing real numbers.

**Output:** This routine returns a vector of the same length of the vectors passed into the routine.  The entries in the vector will be real numbers.  

**Usage/Example:**

The routine takes two arguments. It does not matter which vector is put into the routine first or second. The routine will the return a vector where the 
entries will be X[i] = A[i] + B[i].


**Implementation/Code:** The following is the code for vectorAdd(A, B)


    def vectorAdd(A, B):
        n = len(A)
        x = []
        for i in range(n):
            x.append(A[i] + B[i])
        return x
      
      
    main():
        A = [1, 2, 3]
        B = [3, 4, 5]
        
        print(vectorAdd(A, B))
        
        
    main()
    
    
The code above returns the following output:

    [4, 7, 6]
    
   

**Last Modified:** October/2021

[Back](../README.md)
