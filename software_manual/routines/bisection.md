
**Routine Name:**           bisection

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 bisection.py


**Description/Purpose:** This routine will approximate the root of a function using the bisection method.  A function defined as f(x) must be defined
 before hand for the routine to use. 

**Input:** The input takes real numbers.  The first two inputs, a and b, is the interval you want to search for a root between.  Then, tolerance is how close 
you want the error in the approximation to be.  Last is max iteration which is how many times you want the routine to run before approximating the root 
if the tolerance is not reached. 

**Output:** This routine returns a real number that is the approximation of a root of a given function. If a root is not in the interval or if there 
are multiple roots in the interval an error message will be returned. 

**Usage/Example:**

The routine takes four arguments. The first two are the endpoints of the interval you want to seach for a root in.  The first input should be smaller than the 
second input.  The third input is tolerance and the last is max iterations.  A root must be encompassed in the interval for an approximation to be given.
 There must also be only one root within the given interval or the function will return an error and not find either root, or report an incorrect root. 



**Implementation/Code:** The following is the code for bisection(a, b, tol, maxIter)

    
    def bisection(a, b, tol, maxIter):
        iter = 0
        
        fa = f(a)
        fb = f(b)
        if (fa * fb > 0):
            return "Enter an interval on different sides of one root, a root was not encompassed"
        elif (fa * fb == 0):
            return "You have selected a root with one of your interval boundry points"
        else:
            while (iter < maxIter and abs(fa - fb) > tol):
                c = (a + b) / 2
                fc = f(c)
                if (fa * fc < 0):
                    fb = fc
                    b = c
                    iter += 1
                elif (fb * fc < 0):
                    fa = fc
                    a = c
                    iter += 1
                else:
                    return c
                    
        return c


**Last Modified:** October/2021

[Back](../README.md)
