
**Routine Name:**           findAllRootsHybridMethod

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 findAllRootsHybridMethod.py


**Description/Purpose:** This routine will approximate all of the roots of a function in an interval using a hybrid method.  
A function defined as f(x) must be defined to be passed into the routine. 

**Input:** The input takes real numbers.  The first two inputs, a and b, is the interval you want to search for a root between. The next input is 
the function in which you are searching for the root/roots.
Then, tolerance is how close you want the error in the approximation to be.  Last is max iteration which is how many times you want 
the routine to run before approximating the root if the tolerance is not reached. 

**Output:** This routine returns a list of real number that are the approximations of all roots of a given function in the given interval.
If a root is not in the interval then an empty list will be returned. 

**Usage/Example:**

The routine takes five arguments. The first two are the endpoints of the interval you want to seach for a root in.  The first input should be smaller than the 
second input.  The third input is the function which is passed into the method.
Then tolerance and the last is max iterations.  A root must be encompassed in the interval for an approximation to be given.
 


**Implementation/Code:** The following is the code for findAllRootsHybridMethod(a, b, f, tol, maxIter)



    import math

    def findAllRootsHybridMethod(a, b, f, tol, maxIter):

        roots = []
        x0 = a
        k = 0.01
        x1 = x0 + k

        while x1 < b:

            while (f(x0) * f(x1)) > 0:
                x1 = x1 + k
                if x1 > b:
                    return roots

            c = (x0 + x1) / 2
            fc = f(c)
            if (f(x0) * fc < 0):
                x1 = c

            elif (f(x1) * fc < 0):
                x0 = c

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
            roots.append(x2)

            x0 = x2 + k
            x1 = x0 + k

        return roots



    def main():
        def f(x):
            return math.exp(-(x * x)) * math.sin(4 * (x * x) - 1.0) + 0.051


        result = findAllRootsHybridMethod(-5, 6, f, .01, 10)
        print(result)

    main()


Running the code produces the following output.

        [-1.7271248106401786, -1.7057969683810572, -1.3216144365782123, -1.0392395994090395, -0.4853907192144971, 0.48273332694129023, 1.0344241407567616,
        1.3206433031002394, 1.7101756528739664, 1.722600946325216]
    


**Last Modified:** November/2021

[Back](../README.md)
