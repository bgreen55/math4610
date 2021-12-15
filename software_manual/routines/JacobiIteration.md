
**Routine Name:**           jacobiIteration

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 jacobiIteration.py


**Description/Purpose:** This routine will approximate the solution to a system of linear equations. 

**Input:** The input takes a matrix of all real numbers, the vector b in Ax = b, a guess at the vector x, a tolerance and a max number of iterations. 

**Output:** This routine returns a vector the size of the vectors passed into the routine. 

**Usage/Example:**

The routine takes the five arguments and iterates from the guess vector to an approximate solution to the given system of linear equations. 

**Implementation/Code:** The following is the code for jacobiIteration(A, b, x, tol, maxIter):


    def JacobiIteration(A, b, x, tol, maxIter):
        n = len(b)
        error = tol * 10.0
        iter = 0
        x1 = [0] * n

        while error > tol and iter < maxIter:
            for i in range(n):
                x1[i] = b[i]
                for j in range(i - 1):
                    x1[i] = x1[i] - A[i][j] * x[j]
                for j in range(n):
                    x1[i] = x1[i] - A[i][j] * x[j]
                x1[i] = x1[i] / A[i][i]

            for i in range(n):
                error = error + (x1[i] - x[i]) * (x1[i] - x[i])
            error = math.sqrt(error)
            iter += 1

    
    def main():
        A = [[2, 1], [1, 3]]
        b = [23/2, 17]
        x = [2, 2]

        y = JacobiIteration(A, b, x, .001, 300)
        print(y)


    main()
    
    
The code above returns the following output:

    [2.75, 3.0]
    
This method does not work as well as I would like it too and I want to revisit it.   

**Last Modified:** December/2021

[Back](../README.md)
