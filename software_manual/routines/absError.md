

**Routine Name:**           absError

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 absError.py


**Description/Purpose:** This routine will compute the absolute error of using a number x to approximate a number 
xexact. 

**Input:** The input takes real numbers.  The first input is the approximating number and the second input is the exact number.

**Output:** This routine returns a real number that is the absolute error of the approximating number and the exact number.  

**Usage/Example:**

The routine takes two arguments, the approximating number and the number that is being approximated.  It then takes an absolute value
of the approximating number take away the exact number.  The routine the returns a real number.  



**Implementation/Code:** The following is the code for absError(x, xexact)

    
    def absError(x, xexact):
        error = abs(x - xexact)
        return error
    


**Last Modified:** October/2021

[Back](README.md)
