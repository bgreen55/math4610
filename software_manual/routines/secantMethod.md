
**Routine Name:**           Secant Method

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 secantMethod.py


**Description/Purpose:** This routine will approximate the root of a function using the Secant  method.  A function defined as f(x) must be defined
 before hand for the routine to use. 

**Input:** The input takes real numbers.  The firt two inputs are an interval that contains the root.  Then, tolerance is how close 
you want the error in the approximation to be.  Last is max iteration which is how many times you want the routine to run before approximating the root 
if the tolerance is not reached. 

**Output:** This routine returns a real number that is the approximation of a root of a given function.  If the bound of the approximation of the root are to far
away from the true root, the method will fail to find true root.  


**Usage/Example:**

The routine takes four arguments. The first two are the bounds the root is contained in. The third input is tolerance and the last is max iterations.  
The bounds of the root must be close enough to the true root for the method to converge on the root, or the method will diverge
and report an incorrect root.


**Implementation/Code:** The following is the code for secantMethod(x0, x1, tol, maxIter)

    

    def secantMethod(x0, x1, tol, maxIter):
        f0 = f(x)
        f1 = f(x1)
        error = 10.0 * tol
        icount = 0
        while error > tol and icount < maxIter:
            x2 = x0 - f0 * ((x1 - x0) / (f1 - f0))
            x1 = x - (f0 / df0)
            error = abs(x2 - x1)
            icount = icount + 1
            x0 = x1
            x1 = x2
            f0 = f(x0)
            f1 = f(x1)
        return x2
    
    def main():
        result = newtonsMethod(5, .001, 130)
        print(result)
    
    
    main()   
    
   


**Last Modified:** November/2021

[Back](../README.md)
