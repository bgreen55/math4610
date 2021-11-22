
**Routine Name:**           Newton's Method

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 newtonsMethod.py


**Description/Purpose:** This routine will approximate the root of a function using Newton's method.  A function defined as f(x) must be defined
 before hand for the routine to use. 

**Input:** The input takes real numbers.  The first input is original approximation of the root.  Then, tolerance is how close 
you want the error in the approximation to be.  Last is max iteration which is how many times you want the routine to run before approximating the root 
if the tolerance is not reached. 

**Output:** This routine returns a real number that is the approximation of a root of a given function.  If the original approximation of the root is to far
away from the true root, the method will diverge away from the true root.  


**Usage/Example:**

The routine takes three arguments. The first is the approximation of the root.  The second input is tolerance and the last is max iterations.  The approximation
of the root must be close enough to the true root for the method to converge on the root, or the method will diverge and report an incorrect root.


**Implementation/Code:** The following is the code for newtonsMethod(x, tol, maxIter)

    

    def newtonsMethod(x, tol, maxIter):
        f0 = f(x)
        df0 = df(x)
        error = 10.0 * tol
        icount = 0
        while error > tol and icount < maxIter:
            x1 = x - (f0 / df0)
            error = abs(x1 - x)
            icount = icount + 1
            x = x1
            f0 = f(x)
            df0 = df(x)
        return x1
    
    def main():
        result = newtonsMethod(5, .001, 130)
        print(result)
    
    
    main()   
   


**Last Modified:** November/2021

[Back](README.md)
