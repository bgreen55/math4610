

**Routine Name:**           relError

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 ewlError.py


**Description/Purpose:** This routine will compute the relative error of using a number x to approximate a number 
xexact. 

**Input:** The input takes real numbers.  The first input is the approximating number and the second input is the exact number.

**Output:** This routine returns a real number that is the absolute error of the approximating number and the exact number.  

**Usage/Example:**

The routine takes two arguments, the approximating number and the number that is being approximated.  It then takes an absolute value
of the approximating number take away the exact number.  Then it divides the result by the exact number.  The routine the returns a real number.  



**Implementation/Code:** The following is the code for relError(x, xexact)

    
    def relError(x, xexact):
        error = abs(x - xexact) / xexact
        return error
    


**Last Modified:** October/2021

[Back](README.md)
