
**Routine Name:**           2D Graphics

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 graphics.py


**Description/Purpose:** This routine will plot a graph of up to 5 lines from inputed expressions.

**Input:** The input takes strings.  The user will input up to 5 expressions as stings in the terminal, written in python syntax.
To stop inputing expressions, on an expression enter a blank string.  Then the user will enter how large they want the x axis to be
on their plot.  

**Output:** This routine returns a plot with the graphed lines of the input expressions.  

**Usage/Example:**

The routine takes between 2 and 6 arguments.  It can take any where from 1 to 5 expressions, written in python syntax as strings, and then it takes an integer
 as the largest x bound on the plot.  After the program takes the needed input, it will return one graph with all expresssions graphed and a legend. 



**Implementation/Code:** The following is the code for relError(x, xexact)

    
    def relError(x, xexact):
        error = abs(x - xexact) / xexact
        return error
    


**Last Modified:** October/2021

[Back](README.md)
