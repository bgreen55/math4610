
**Routine Name:**           Task 1 Task Sheet 6

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 modedHybridMethod.py


**Description/Purpose:** This routine runs the four root finding methods funcIter, bisection, newtons method and secant method to approximate a root of the 
given function. 

**Input:** The code does not take any input.  The functions in the routine that take input have already been provided with the input they need.

**Output:** This routine returns four real numbers that are the approximation of the closest root to zero. 


**Usage/Example:**

The routine is used to test how each method for calcuating roots works. Different functions can be plugged into the code to find the roots of different 
functions. 



**Implementation/Code:** 


    import math


    def f(x):
        return math.exp(-(x * x)) * math.sin(4 * (x * x) - 1.0) + 0.051


    def df(x):
        return -2 * x * math.exp(-(x * x)) * (math.sin(4 * (x * x) - 1.0)) - 4 * math.cos(4 * (x * x) - 1.0)


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


    def secantMethod(x0, x1, tol, maxIter):
        f0 = f(x0)
        f1 = f(x1)
        error = 10.0 * tol
        icount = 0
        while error > tol and icount < maxIter:
            x2 = x0 - f0 * ((x1 - x0) / (f1 - f0))
            error = abs(x2 - x1)
            icount = icount + 1
            x0 = x1
            x1 = x2
            f0 = f(x0)
            f1 = f(x1)
        return x2


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


    def funcIter(xnot, tol, maxIter):
        iter = 0
        error = 10.0 * tol

        while error > tol and iter < maxIter:
            x = f(xnot)
            error = abs(x - xnot)
            xnot = x
            iter = iter + 1

        return x


    def main():

        bi = bisection(0, 1, .000001, 100)

        fi = funcIter(0.1, .001, 100)

        ne = newtonsMethod(.4, .001, 10)

        se = secantMethod(.1, .8, .001, 10)

        print("bisection method")
        print(bi)
        print('functional iteration')
        print(fi)
        print("newtons method")
        print(ne)
        print("secant Method")
        print(se)


    main()


The output of running the code prints the following output. 

    bisection method
    0.4836108684539795
    functional iteration
    -0.4747690413043361
    newtons method
    -0.4833702080017816
    secant Method
    0.48361076657793556

    


**Last Modified:** November/2021

[Back](../README.md)
