
**Routine Name:**           SecantHybridMethod

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 SecantHybridMethod.py


**Description/Purpose:** This routine will approximate the root of a function using a hybrid method.  A function defined as f(x) must be defined
 to be passed into the routine. This hybrid method uses the secant method rather than newton's method as a way of approximating the root.  

**Input:** The input takes real numbers.  The first two inputs, a and b, is the interval you want to search for a root between. The next input is the function
in which you are searching for the root.
Then, tolerance is how close you want the error in the approximation to be.  Last is max iteration which is how many times you want 
the routine to run before approximating the root if the tolerance is not reached. 

**Output:** This routine returns a real number that is the approximation of a root of a given function. If a root is not in the interval or if there 
are multiple roots in the interval an error message will be returned. 

**Usage/Example:**

The routine takes five arguments. The first two are the endpoints of the interval you want to seach for a root in.  The first input should be smaller than the 
second input.  The third input is the function passed into the method.
Then tolerance and the last is max iterations.  A root must be encompassed in the interval for an approximation to be given.
 There must also be only one root within the given interval or the function will return an error and not find either root, or report an incorrect root. 



**Implementation/Code:** The following is the code for secantHybridMethod(x0, x1, f, tol, maxIter)


    import math

    def secantHybridMethod(x0, x1, f, tol, maxIter):
        f0 = f(x0)
        f1 = f(x1)
        error = 10.0 * tol
        icount = 0
        while error > tol and icount < maxIter:
            try:
                x2 = x0 - f0 * ((x1 - x0) / (f1 - f0))
            except:
                x0 = 0
                k = .01
                x1 = x0 + k
                while f(x0) * f(x1) > 0:
                    x1 = x1 + k
                f0 = f(x0)
                f1 = f(x1)
                x2 = x0 - f0 * ((x1 - x0) / (f1 - f0))

            error = abs(x2 - x1)
            icount = icount + 1
            x0 = x1
            x1 = x2
            f0 = f(x0)
            f1 = f(x1)
        return x2

    def main():
        def f(x):
            return math.exp(-(x * x)) * math.sin(4 * (x * x) - 1.0) + 0.051

        result = secantHybridMethod(-5, 6, f, .01, 10)
        print(result)

    main()

 
The code produces the following output.

        0.48360372739336516
    


**Last Modified:** November/2021

[Back](../README.md)
