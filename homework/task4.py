# approximation of the second derivative of cos(x)

import math


def secondOrderApprox(x, h):
    output = (math.cos(x + h) - (2 * (math.cos(x))) + (math.cos(x - h))) / (h * h)
    return output



def main():
    x = 2
    h = 1
    h2 = .5


    print("Iter" + "%4s" % "h" + "%15s" % "Approx" + "%25s" % "Error")
    print()

    print("1      " + str(h) + "         " + str(secondOrderApprox(x, h)) + "       " + str(-math.cos(x) - secondOrderApprox(x, h)))
    print("2      " + str(h2) + "       " + str(secondOrderApprox(x, h2)) + "        " + str(-math.cos(x) - secondOrderApprox(x, h2)))

    for i in range(16):
        # the i + 3 gives which iteration the loop is in since the first 2 iterations happen outside the loop
        msg = (secondOrderApprox(x, (10 ** (-(i + 1)))))
        if msg != 0:
            print(str(i + 3) + "      " + "10e" + str(-(i + 1)) + "     " + str(msg) + "         " + str(-math.cos(x) - msg))
        else:
            print(str(i + 3) + "      " + "10e" + str(-(i + 1)) + "     " + str(msg) + "                       " + str(-math.cos(x) - msg))


main()
