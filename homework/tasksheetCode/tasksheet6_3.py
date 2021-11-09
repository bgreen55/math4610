
# task three for tasksheet6 math 4610
# finds the closest root to 0
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
