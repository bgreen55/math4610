
**Routine Name:**           funcIter

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 funcIter.py


**Description/Purpose:** This routine will use functional iteration to approximate a root of a function. A fucntion f(x) that takes x as the x variable in a 
funtion must be defined before hand. 

**Input:** The input takes real numbers.  The first input of the function(xnot) is your guess of the root. The second input is the tolerance you want to have 
in the approximation of the root and the last input to the function is the maximum number of iterations you want the function to run if the tolerance in the 
error of the approximation has not been met before giving the approximation. 

**Output:** This routine returns a real number that is the approximation of the root of the function.  

**Usage/Example:**

The routine takes three arguments.  It can be used to approximate the closest root to xnot of a given function.  However, as function complexity increases
such as x being raised by e, the routine will begin to fail in its approximation of a root.



**Implementation/Code:** The following is the code for funcIter(xnot, tol, maxIter)

    
    def funcIter(xnot, tol, maxIter):
        iter = 0
        error = 10.0 * tol
        
        while error > tol and iter < maxIter:
            x = f(xnot)
            error = abs(x - xnot)
            xnot = x
            iter = iter + 1
            
        return x
        
        
      

**Last Modified:** October/2021

[Back](README.md)
