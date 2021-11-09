# task 4 for tasksheet 6

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

