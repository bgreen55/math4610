
**Routine Name:**           scalarMultVector

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 scalarMultVector.py


**Description/Purpose:** This routine will multiply a scalar to a vector.

**Input:** The input takes a real numbered scalar and then a vector containing real numbers.

**Output:** This routine returns a vector of the same length of the vector passed into the routine.  The entries in the vector will be real numbers.  

**Usage/Example:**

The routine takes two arguments.  The first argument has to be the scalar and the second had to be the vector.  The routine will then multiply the scalar 
to every entry in the vector and return the new vector.


**Implementation/Code:** The following is the code for scalarMultVector(a, B)


    def scalarMultVector(a, B):
        n = len(B)
        x = []
        for i in range(n):
            x.append(a * B[i])
        return x
      
      
    main():
        a = 2
        B = [3, 4, 5]
        
        print(scalarMultVector(a, B))
        
        
    main()
    
    
The code above returns the following output:

    [6, 8, 10]
    
   

**Last Modified:** December/2021

[Back](../README.md)
