# task 5 find all roots in the interval

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

    def df(x):
        return -2 * x * math.exp(-(x * x)) * (math.sin(4 * (x * x) - 1.0)) - 4 * math.cos(4 * (x * x) - 1.0)

    result = findAllRootsHybridMethod(-5, 6, f, .01, 10)
    print(result)

main()
