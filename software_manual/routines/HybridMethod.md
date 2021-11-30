
**Routine Name:**           HybridMethod

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 hybridMethod.py


**Description/Purpose:** This routine will approximate the root of a function using a hybrid method.  A function defined as f(x) and its derivative must be defined
 to be passed into the routine. 

**Input:** The input takes real numbers.  The first two inputs, a and b, is the interval you want to search for a root between. The next input x0 is the 
best apporximation of where the root is.  The next to inputs are used to pass in the function and its derivative in which you are searching for the root.
Then, tolerance is how close you want the error in the approximation to be.  Last is max iteration which is how many times you want 
the routine to run before approximating the root if the tolerance is not reached. 

**Output:** This routine returns a real number that is the approximation of a root of a given function. If a root is not in the interval or if there 
are multiple roots in the interval an error message will be returned. 

**Usage/Example:**

The routine takes seven arguments. The first two are the endpoints of the interval you want to seach for a root in.  The first input should be smaller than the 
second input.  The third input is an approximation of the root.  Then the function and its derivative are passed into the method.
Then tolerance and the last is max iterations.  A root must be encompassed in the interval for an approximation to be given.
 There must also be only one root within the given interval or the function will return an error and not find either root, or report an incorrect root. 



**Implementation/Code:** The following is the code for hybridMethod(a, b, x0, f, df, tol, maxIter)


    
    def hybridMethod(a, b, x0, f, df, tol, maxIter):

        fa = f(a)
        fb = f(b)
        if (fa * fb > 0):
            return "error"
        if (x0 < a or x0 > b):
            return "error"

        f0 = f(x0)
        df0 = df(x0)
        error = 10.0 * tol
        icount = 0

        while (error > tol and icount < maxIter):
            x1 = x0 - f0 / df0
            errnewt = abs(x1 - x0)
            if (errnewt > error):
                for i in range(4):
                    c = 0.5 * (a + b)
                    fc = f(c)
                    if (fa * fc < 0):
                        b = c
                        fb = fc
                    else:
                        a = c
                        fa = fc

                error = b - a
                x0 = c
                f0 = fc
                df0 = df(c)

            icount = icount + 1

        return x1


    def main():

        def f(x):
            return (x * x) - 3

        def df(x):
            return 2 * x

        result = hybridMethod(-1, 15, 4, f, df, .01, 10)
        print(result)


    main()


Running the routine above results in approximating a root at 1.75.  The actual root of the fuction is approximately 1.7321, meaning our hyrbrid approximation
 of the root had a close approximation.


**Last Modified:** November/2021

[Back](../README.md)
