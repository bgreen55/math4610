
**Routine Name:**           dmaceps

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 dmaceps.py


**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to
return values in those variables.

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

The routine has no arguments.  It runs an iteration dividing 1 in half each iteration and adding that number, epsilon, to 1.  Once epsilon is so that 
epsilon plus 1 equals 1 the iteration breaks.  Each iteration before hand prints out including the size of epsilon in 64 bit size. 



**Implementation/Code:** The following is the code for dmaceps()

    def dmaceps():
    x = 1
    epsilon = float(0.5)
    for i in range(100):
        xapprox = float(x + epsilon)
        error = float(abs(x - xapprox))
        if error == 0:
            break
        else:
            epsilon = float(epsilon / 2)
            print(i, error)

dmaceps()



**Last Modified:** September/2021
