
**Routine Name:**           ModedHybridMethod

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 modedHybridMethod.py


**Description/Purpose:** This routine will approximate the root of a function using a hybrid method.  A function defined as f(x) and its derivative must be defined
 to be passed into the routine. This implementation of the hybrid method works better than our previous implementation of the hybrid method. 

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



**Implementation/Code:** The following is the code for modedHybridMethod(a, b, x0, f, df, tol, maxIter)


    import math

    def modedHybridMethod(a, b, x0, f, df, tol, maxIter):
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

                w = 0
                k = 0.01
                t = w + k
                fw = f(w)
                ft = f(t)

                while (fw * ft > 0):
                    t = t + k
                    ft = f(t)

                error = t - w
                x0 = t
                f0 = ft
                df0 = df(t)

            icount = icount + 1
        return x1


    def main():
        def f(x):
            return math.exp(-(x * x)) * math.sin(4 * (x * x) - 1.0) + 0.051

        def df(x):
            return (-2 * x * math.exp(-(x * x))) * ((math.sin(4 * (x * x) - 1.0)) - (4 * math.cos(4 * (x * x) - 1.0)))

        result = modedHybridMethod(-5, 6, .01, f, df, .01, 10)
        print(result)

    main()


This code produces the following output.

        0.4836167095695605
    

**Last Modified:** November/2021

[Back](../README.md)
