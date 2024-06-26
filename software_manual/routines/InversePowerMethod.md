
**Routine Name:**           inversePowerMethod

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 inversePowerMethod.py


**Description/Purpose:** This routine will use the power method to compute the largest eigenvalue of the inverse of a matrix to find the smallest eigenvalue 
of the given matrix.

**Input:** The input is a matrix of size nxn, a vector of length n, a guess of the eigenvalue, a tolerance and maxIteration. 

**Output:** This routine returns a real number which is the approximation of the smallest eigenvalue for the matrix. 

**Usage/Example:**

We gave the routine a random 100x100 symmetric diagonally dominant matrix, with a vector of length 100 and a lambda guess of 1, tolerance of .001 and max 
iteration of 20.  When the routine ran the output below is what we got. 


**Implementation/Code:** The following is the code for inversePowerMethod(A, x, lam, tol, maxIter):


    import math
    from random import randint


    def inversePowerMethod(A, x, lam, tol, maxIter):
        error = 10.0 * tol
        icount = 0

        while error > tol and icount < maxIter:
            y = GEAndBackSubScaledPivot(A, x)
            w = scalarMultVector((1 / vectorMagL2(y)), y)

            q = GEAndBackSubScaledPivot(A, w)
            lam1 = dotProduct(w, q)
            error = abs(lam1 - lam)
            lam = lam1
            x = w
            icount += 1

        return lam
        
     
    def main():
         l = 3

         B = diagSymMatrix(100)
         b = [0] * 100
         b[0] = 1

         ipMethod = inversePowerMethod(B, b , l, .001, 200)
         print("Inverse Power Method finds smallest eigenvalue")
         print(ipMethod)


    # A is a vector
    def vectorMagL2(A):
        n = len(A)
        x = 0
        for i in range(n):
            x = x + (A[i] * A[i])
        ans = math.sqrt(x)
        return ans


    def dotProduct(A, B):
        n = len(A)
        x = 0
        for i in range(n):
            x += A[i] * B[i]
        return x


    # a is the scalar and B is the vector
    def scalarMultVector(a, B):
        n = len(B)
        x = []
        for i in range(n):
            x.append(a * B[i])
        return x


    def transposeMatrix(A):
        n = len(A)      # 3
        m = len(A[0][:])     # 2
        x = []
        # create empty transposed matrix as x
        for i in range(m):
            a = []
            for j in range(n):
                a.append(None)
            x.append(a)
        # take values from A and put them in the transposed matrix
        for i in range(m):
            for j in range(n):
                x[i][j] = A[j][i]

        return x


    def GEAndBackSubScaledPivot(A, b):
        # Ax = b is the matrix form
        n = len(b)
        s = [None] * n

        # gaussian elimination
        for i in range(0, n, 1):
            s[i] = abs(A[i][0])
            for j in range(0, n, 1):
                temp1 = abs(A[i][j])
                if temp1 > s[i]:
                    s[i] = temp1

        for k in range(0, n - 1, 1):
            temp1 = abs(A[k][k] / s[k])
            q = k
            for i in range(k + 1, n, 1):
                temp2 = abs(A[i][k] / s[i])
                if temp1 < temp2:
                    temp1 = temp2
                    q = i

            temp1 = b[k]
            b[k] = b[q]
            b[q] = temp1
            temp1 = s[k]
            s[k] = s[q]
            s[q] = temp1

            for j in range(0, n, 1):
                temp1 = A[k][j]
                A[k][j] = A[q][j]
                A[q][j] = temp1

            for i in range(k + 1, n, 1):
                factor = A[i][k] / A[k][k]
                for j in range(k, n, 1):
                    A[i][j] = A[i][j] - factor * A[k][j]
                b[i] = b[i] - factor * b[k]

        # back substitution
        length = len(b)
        x = [None] * length

        m = length - 1
        x[m] = b[m] / A[m][m]
        for i in range(m - 1, -1, -1):
            sum = b[i]
            for j in range(i + 1, n, 1):
                sum = sum - A[i][j] * x[j]
            x[i] = sum / A[i][i]

        return x


    def diagSymMatrix(n):
        A = []
        for i in range(n):
            x = []
            for j in range(n):
                if j == i:
                    value = 0
                    x.append(value)
                elif j > i:
                    value = randint(0, 9)
                    x.append(value)
                else:
                    value = A[j][i]
                    x.append(value)
            A.append(x)

        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum = sum + A[i][j]

            if A[i][i] <= sum:
                value = randint(sum, sum + 10)
                A[i][i] = value

        for i in range(n):
            for j in range(n):
                print(A[i][j], end=" ")
            print()
        print()
        # returning the matrix A allows it to be used by other funcitons
        return A


    main()


    
The code above returns the following output:

    
    465 2 7 9 8 9 6 6 3 9 9 7 0 2 7 2 2 8 7 7 1 2 5 5 5 6 2 0 7 4 0 1 7 7 4 8 1 2 0 3 7 2 0 7 8 8 1 1 9 7 9 7 6 7 3 4 6 8 5 6 1 3 1 6 3 1 1 9 2 4 1 0 7 3 0 2 7 5 8 4 4 1 4 3 1 9 6 1 9 9 5 8 9 4 1 8 8 2 7 4 
    2 462 8 4 9 9 0 1 8 1 8 8 6 6 7 4 7 7 5 0 3 3 9 2 3 3 2 1 9 9 3 5 0 8 3 2 9 4 0 2 8 6 7 3 9 6 6 8 5 8 6 6 5 7 6 0 8 6 9 3 1 3 3 6 0 6 9 1 7 5 8 2 3 0 2 5 1 4 9 1 6 0 0 1 5 8 8 0 7 2 7 9 6 8 7 2 1 0 1 3 
    7 8 455 9 1 5 6 4 5 0 0 1 5 2 5 5 1 2 3 6 0 6 2 1 9 5 0 3 2 3 9 8 2 7 3 4 6 4 0 8 6 2 1 1 3 9 9 9 1 7 8 1 7 7 9 7 0 8 0 4 2 7 7 6 2 2 8 3 3 5 6 9 5 4 0 4 8 2 4 2 9 2 4 8 0 4 5 9 9 1 3 9 1 5 8 8 7 3 8 2 
    9 4 9 452 3 5 7 5 8 3 7 0 4 6 1 1 2 8 2 6 2 4 1 3 3 4 9 0 6 8 9 1 3 3 9 2 6 2 6 9 6 2 4 9 9 2 2 2 6 4 9 0 3 6 1 3 6 2 0 8 8 2 8 3 2 1 2 8 9 9 5 2 2 7 8 3 8 1 2 9 0 1 9 7 5 7 5 2 5 6 3 6 3 4 6 2 5 2 3 2 
    8 9 1 3 477 8 6 7 1 5 6 6 3 7 1 2 2 6 0 6 0 1 4 7 9 3 8 5 7 5 1 1 7 4 9 9 4 9 6 3 4 0 5 3 0 1 6 3 6 9 0 3 1 8 4 7 8 3 4 7 9 2 8 7 9 5 1 6 6 6 6 0 2 8 9 9 4 4 1 9 4 6 8 6 5 5 2 4 7 4 9 6 8 0 4 6 0 3 8 0 
    9 9 5 5 8 494 9 9 6 1 2 5 2 3 9 5 0 9 7 0 4 9 0 6 1 0 4 4 8 4 9 6 3 9 9 0 5 5 7 6 3 8 4 0 1 9 6 9 9 1 6 1 3 2 6 8 9 1 2 1 4 9 0 7 5 8 2 8 2 7 0 4 7 6 4 9 6 1 0 0 9 4 6 9 0 1 8 7 9 4 5 3 5 7 6 8 9 0 7 6 
    6 0 6 7 6 9 405 8 9 9 2 4 5 1 8 1 2 5 3 9 1 6 5 3 2 8 2 8 3 1 6 3 7 2 3 2 5 0 4 2 0 8 6 5 1 1 4 3 8 2 5 2 8 6 7 3 9 8 0 0 0 5 4 8 2 3 5 2 6 7 4 1 6 2 0 0 6 6 2 7 7 0 0 0 0 0 5 2 9 3 2 2 4 4 8 8 1 6 1 1 
    6 1 4 5 7 9 8 503 6 8 4 9 0 9 8 6 4 2 5 0 9 5 6 5 6 4 8 9 4 6 2 8 9 1 8 5 6 1 1 1 7 9 1 8 4 5 7 9 2 3 8 7 5 8 0 5 3 4 4 0 6 1 9 1 8 5 5 3 7 8 8 7 6 7 8 9 5 5 7 1 3 3 2 7 5 4 6 2 6 6 4 2 2 7 4 2 0 1 5 8 
    3 8 5 8 1 6 9 6 456 3 4 8 7 7 3 8 7 3 2 2 2 3 8 9 6 0 3 0 7 9 2 4 1 3 1 5 2 9 1 0 3 6 1 1 6 1 0 6 0 7 5 2 7 8 3 6 4 6 8 6 0 8 1 9 5 5 1 9 9 6 0 6 4 3 4 5 3 5 6 2 4 5 2 4 6 7 1 8 5 9 3 1 3 5 9 3 8 9 8 1 
    9 1 0 3 5 1 9 8 3 457 1 2 9 8 5 7 7 8 6 4 2 4 8 6 1 1 9 0 5 1 0 3 0 4 1 4 1 8 0 4 8 5 0 9 9 4 1 5 1 5 9 5 2 2 5 4 1 7 9 2 7 9 5 8 1 7 5 2 7 9 3 6 8 4 9 8 8 3 8 7 1 3 2 1 4 6 4 5 6 0 1 6 3 8 8 5 7 1 1 3 
    9 8 0 7 6 2 2 4 4 1 432 4 1 4 9 7 7 4 5 3 0 3 2 4 3 7 5 0 6 9 5 0 9 9 9 7 2 9 6 9 3 0 0 7 7 3 5 6 1 6 7 0 4 2 6 0 6 3 3 0 0 3 1 3 9 1 9 7 9 9 1 0 3 3 9 7 5 5 0 1 6 9 1 1 4 1 7 6 7 3 1 6 6 0 6 5 3 3 8 0 
    7 8 1 0 6 5 4 9 8 2 4 414 6 2 8 2 8 2 6 7 9 5 2 2 4 3 3 0 0 3 3 0 9 7 8 4 1 4 1 0 8 3 8 2 3 3 0 9 2 6 7 1 3 7 0 2 9 6 4 5 5 9 1 8 0 4 6 0 4 0 2 6 6 4 2 6 1 0 2 1 5 7 2 9 3 2 2 8 8 4 5 6 7 2 9 2 8 1 3 0 
    0 6 5 4 3 2 5 0 7 9 1 6 446 1 1 8 3 1 9 7 7 3 8 9 5 4 6 5 0 7 1 2 6 1 8 2 8 6 1 8 2 4 2 4 7 6 8 5 1 1 1 6 5 3 2 8 6 5 6 1 4 4 3 1 2 1 3 3 8 0 3 8 8 4 8 3 5 8 0 9 4 6 5 4 1 6 8 8 3 2 9 5 9 5 5 1 4 2 5 6 
    2 6 2 6 7 3 1 9 7 8 4 2 1 478 3 5 0 3 2 1 6 0 4 1 8 5 3 6 7 5 8 6 8 3 7 9 3 5 9 4 2 6 2 1 9 2 9 2 8 4 8 8 9 6 4 9 9 4 2 3 8 6 7 6 7 4 6 9 1 5 5 2 5 2 6 8 5 0 1 0 9 6 5 1 5 1 0 0 3 2 5 8 5 4 8 6 8 4 3 7 
    7 7 5 1 1 9 8 8 3 5 9 8 1 3 484 8 1 5 2 5 9 5 7 1 9 4 7 9 2 2 9 7 4 7 9 4 2 2 8 8 5 8 3 9 2 7 6 1 7 8 2 8 2 6 0 0 1 6 1 7 2 6 3 2 8 2 0 8 6 0 9 3 0 5 5 4 0 6 6 3 6 4 5 9 6 7 9 9 2 1 7 4 1 0 5 9 0 9 5 2 
    2 4 5 1 2 5 1 6 8 7 7 2 8 5 8 462 0 0 6 5 1 8 9 9 8 8 6 5 7 8 6 4 1 6 1 8 1 0 3 5 5 4 8 4 0 3 9 3 9 6 5 5 1 7 1 6 8 2 4 3 2 3 8 3 3 9 3 5 3 3 1 2 3 4 1 6 2 9 4 9 8 0 5 6 3 9 4 0 7 1 6 9 2 8 1 6 8 3 3 9 
    2 7 1 2 2 0 2 4 7 7 7 8 3 0 1 0 442 7 0 0 7 3 5 3 5 0 3 0 5 5 0 8 0 3 1 7 3 2 7 6 2 2 5 6 7 5 7 3 4 5 4 3 6 2 3 6 7 3 9 7 6 1 9 3 6 9 7 7 3 2 0 0 5 9 4 3 2 2 6 1 8 9 3 9 7 4 2 9 1 8 8 8 9 5 6 6 9 9 4 3 
    8 7 2 8 6 9 5 2 3 8 4 2 1 3 5 0 7 461 8 3 5 0 4 9 5 1 1 4 9 3 5 5 9 0 2 6 0 4 8 3 6 2 6 1 6 3 9 0 8 5 2 5 7 5 5 4 4 9 8 1 0 8 1 8 0 3 8 2 9 7 2 5 7 7 2 1 6 8 5 8 4 1 9 4 3 4 0 8 3 5 0 7 4 4 5 5 4 5 5 4 
    7 5 3 2 0 7 3 5 2 6 5 6 9 2 2 6 0 8 409 2 1 6 2 2 2 7 9 5 5 7 4 5 4 4 5 3 6 1 9 8 5 6 3 4 7 8 3 7 0 1 5 1 7 5 2 3 2 3 9 8 0 8 9 3 6 8 0 0 1 7 4 7 3 6 5 5 0 4 4 3 4 1 7 2 2 0 5 6 6 8 1 1 4 0 0 1 4 4 3 2 
    7 0 6 6 6 0 9 0 2 4 3 7 7 1 5 5 0 3 2 440 4 5 1 2 4 6 0 7 3 8 7 8 6 0 5 3 4 6 7 8 7 5 8 3 4 5 1 8 5 1 6 1 5 8 5 8 7 4 9 7 3 3 7 9 0 3 5 7 7 9 2 0 5 5 4 1 7 7 1 2 2 2 7 6 1 2 0 7 0 4 2 7 2 3 3 8 2 2 2 9 
    1 3 0 2 0 4 1 9 2 2 0 9 7 6 9 1 7 5 1 4 467 4 4 8 7 9 1 1 2 7 4 7 2 9 8 7 3 9 4 0 8 9 6 4 1 5 6 2 8 7 9 4 7 4 1 9 0 4 1 8 5 5 3 4 9 2 6 6 4 5 1 5 5 2 6 8 7 9 3 8 6 7 5 2 2 3 6 3 0 4 1 4 5 9 8 2 9 5 4 1 
    2 3 6 4 1 9 6 5 3 4 3 5 3 0 5 8 3 0 6 5 4 418 1 8 8 0 0 3 0 9 1 0 2 0 0 2 0 1 3 2 2 3 9 0 9 9 7 7 5 2 4 2 9 6 6 7 9 9 5 2 5 5 9 9 6 4 6 2 1 8 6 6 6 4 4 4 3 2 2 8 2 0 2 3 1 6 5 0 9 5 9 2 1 2 1 2 2 5 8 9 
    5 9 2 1 4 0 5 6 8 8 2 2 8 4 7 9 5 4 2 1 4 1 463 5 5 3 9 5 9 0 5 3 2 5 9 9 1 0 4 9 8 5 5 9 1 2 6 9 7 7 0 2 6 6 4 4 0 3 6 1 2 8 6 8 5 1 4 5 2 9 7 8 0 6 8 9 9 6 3 7 0 4 3 3 9 8 5 3 1 2 8 0 9 0 5 8 7 0 3 1 
    5 2 1 3 7 6 3 5 9 6 4 2 9 1 1 9 3 9 2 2 8 8 5 426 6 8 2 9 3 1 0 4 6 7 6 1 6 3 3 3 2 0 0 2 6 5 3 0 5 6 9 3 4 9 0 4 1 5 0 0 7 3 6 3 4 0 1 8 1 5 4 4 8 2 7 0 9 8 7 7 9 3 5 3 7 4 3 2 1 5 3 9 5 8 0 0 2 2 7 9 
    5 3 9 3 9 1 2 6 6 1 3 4 5 8 9 8 5 5 2 4 7 8 5 6 500 5 5 7 0 0 8 1 3 6 5 6 2 9 8 7 9 5 1 5 4 0 1 5 2 3 6 8 0 7 5 7 3 1 4 8 8 7 7 5 3 8 2 9 3 1 8 2 6 0 5 6 2 5 5 6 9 9 3 6 4 0 3 5 7 7 7 9 7 1 7 0 3 9 9 9 
    6 3 5 4 3 0 8 4 0 1 7 3 4 5 4 8 0 1 7 6 9 0 3 8 5 435 3 6 3 5 8 2 5 7 4 7 1 4 4 5 4 8 2 1 0 1 1 2 0 1 6 5 5 8 5 1 9 8 1 8 6 0 4 3 4 2 3 2 4 2 7 4 7 4 9 8 0 7 8 7 6 6 6 7 2 8 5 7 8 9 6 1 0 5 0 8 0 0 7 1 
    2 2 0 9 8 4 2 8 3 9 5 3 6 3 7 6 3 1 9 0 1 0 9 2 5 3 431 5 9 2 0 5 1 5 1 7 5 0 4 1 3 6 0 0 7 0 1 9 4 5 2 3 1 8 6 3 7 4 3 8 5 1 8 4 5 3 8 2 1 1 8 1 6 6 9 9 8 2 5 8 8 0 5 9 3 6 1 8 8 4 9 6 0 0 4 1 0 8 9 2 
    0 1 3 0 5 4 8 9 0 0 0 0 5 6 9 5 0 4 5 7 1 3 5 9 7 6 5 411 3 2 8 5 8 8 0 6 3 0 3 5 7 5 7 6 6 9 8 5 2 7 3 5 3 8 8 9 7 3 0 5 5 6 3 7 2 9 0 0 7 0 7 0 4 2 7 4 6 8 3 2 2 1 3 4 7 0 4 2 4 8 2 1 6 1 0 4 1 0 5 0 
    7 9 2 6 7 8 3 4 7 5 6 0 0 7 2 7 5 9 5 3 2 0 9 3 0 3 9 3 439 9 4 1 7 2 6 9 1 0 4 0 0 7 4 0 7 1 9 9 6 9 7 4 5 1 1 4 4 3 5 4 3 0 9 3 4 5 2 4 3 3 3 8 2 9 0 8 7 1 1 0 7 3 9 9 4 0 1 9 6 7 0 5 9 1 7 1 3 1 5 8 
    4 9 3 8 5 4 1 6 9 1 9 3 7 5 2 8 5 3 7 8 7 9 0 1 0 5 2 2 9 473 2 9 6 9 1 4 6 1 5 3 2 9 8 6 0 1 1 7 6 3 9 6 8 9 8 0 2 7 1 6 1 1 1 9 7 8 3 1 2 3 8 5 7 0 8 9 6 6 9 8 0 3 3 6 5 6 2 5 5 6 0 9 9 7 2 1 7 0 0 6 
    0 3 9 9 1 9 6 2 2 0 5 3 1 8 9 6 0 5 4 7 4 1 5 0 8 8 0 8 4 2 434 1 4 0 3 2 8 4 9 9 4 1 8 6 3 7 2 0 7 9 7 2 1 8 5 0 9 9 1 1 9 5 7 0 1 3 8 6 4 3 3 6 9 6 8 6 2 1 6 3 0 2 7 6 6 1 7 7 0 2 0 1 3 9 7 5 3 3 5 2 
    1 5 8 1 1 6 3 8 4 3 0 0 2 6 7 4 8 5 5 8 7 0 3 4 1 2 5 5 1 9 1 439 1 8 6 4 3 4 5 5 3 3 5 3 0 9 8 6 7 6 1 6 3 0 1 4 3 7 4 7 1 9 2 4 2 2 7 0 8 3 6 9 6 3 2 2 6 8 7 9 0 2 7 2 9 4 5 1 1 7 5 6 2 5 8 9 4 9 2 9 
    7 0 2 3 7 3 7 9 1 0 9 9 6 8 4 1 0 9 4 6 2 2 2 6 3 5 1 8 7 6 4 1 466 7 5 0 8 4 6 0 8 5 5 6 1 9 9 9 4 1 9 7 5 2 5 6 9 5 3 0 4 4 1 2 5 9 1 7 7 4 1 7 8 6 0 6 3 7 9 0 5 5 0 0 4 5 9 4 4 9 4 1 8 5 7 3 1 5 3 4 
    7 8 7 3 4 9 2 1 3 4 9 7 1 3 7 6 3 0 4 0 9 0 5 7 6 7 5 8 2 9 0 8 7 496 3 6 8 5 9 7 0 6 0 7 4 7 6 7 0 9 8 9 0 5 9 0 3 5 2 4 1 5 8 4 3 1 5 3 9 7 5 7 3 0 2 9 0 4 2 5 6 5 8 7 7 2 9 2 5 5 7 9 3 6 6 9 8 1 3 9 
    4 3 3 9 9 9 3 8 1 1 9 8 8 7 9 1 1 2 5 5 8 0 9 6 5 4 1 0 6 1 3 6 5 3 451 8 5 8 2 7 2 3 3 5 4 8 2 4 0 8 6 8 5 8 7 8 6 2 9 2 1 0 2 8 3 1 0 6 3 8 2 6 0 9 6 1 1 9 4 2 4 2 2 0 5 6 9 5 4 6 9 1 0 1 6 5 6 4 1 1 
    8 2 4 2 9 0 2 5 5 4 7 4 2 9 4 8 7 6 3 3 7 2 9 1 6 7 7 6 9 4 2 4 0 6 8 470 2 6 0 5 2 4 9 8 2 1 1 4 5 9 5 9 0 6 1 4 6 5 8 4 6 9 4 0 8 6 5 0 6 2 4 0 6 3 3 6 1 6 2 8 3 4 4 4 5 9 4 2 1 4 3 9 6 9 7 4 9 9 2 4 
    1 9 6 6 4 5 5 6 2 1 2 1 8 3 2 1 3 0 6 4 3 0 1 6 2 1 5 3 1 6 8 3 8 8 5 2 466 9 8 7 9 7 8 3 9 6 0 1 1 9 4 2 7 1 8 0 3 7 9 8 2 7 1 1 7 2 3 1 0 7 6 2 7 8 5 7 8 9 9 0 5 6 6 8 8 8 4 9 1 6 8 5 2 6 4 1 3 8 1 3 
    2 4 4 2 9 5 0 1 9 8 9 4 6 5 2 0 2 4 1 6 9 1 0 3 9 4 0 0 0 1 4 4 4 5 8 6 9 439 2 6 8 8 3 3 5 8 4 5 8 9 3 3 6 7 7 6 0 4 4 1 9 3 9 0 8 7 4 4 2 7 8 3 2 9 0 2 9 5 9 4 0 0 3 2 7 3 6 7 3 2 4 2 8 2 4 8 1 3 2 2 
    0 0 0 6 6 7 4 1 1 0 6 1 1 9 8 3 7 8 9 7 4 3 4 3 8 4 4 3 4 5 9 5 6 9 2 0 8 2 417 4 9 1 1 1 5 6 6 7 0 5 0 2 2 4 2 6 8 7 2 6 2 3 9 3 6 6 1 9 1 5 5 3 4 3 2 8 7 8 7 1 1 4 5 2 2 1 3 3 9 2 9 0 4 1 4 1 2 2 2 6 
    3 2 8 9 3 6 2 1 0 4 9 0 8 4 8 5 6 3 8 8 0 2 9 3 7 5 1 5 0 3 9 5 0 7 7 5 7 6 4 434 0 6 5 5 2 6 0 0 1 5 5 2 7 9 4 9 6 7 8 4 0 8 0 2 4 2 9 5 0 4 3 9 9 3 7 6 9 2 3 8 3 0 4 6 5 6 0 5 4 0 6 5 4 4 0 0 1 9 0 3 
    7 8 6 6 4 3 0 7 3 8 3 8 2 2 5 5 2 6 5 7 8 2 8 2 9 4 3 7 0 2 4 3 8 0 2 2 9 8 9 0 461 1 7 5 0 6 8 2 7 0 2 6 3 8 7 7 5 7 9 0 0 4 6 2 4 6 3 0 7 5 5 7 0 5 0 5 9 8 2 7 6 9 1 2 4 1 6 0 6 5 7 4 8 8 0 8 8 1 9 6 
    2 6 2 2 0 8 8 9 6 5 0 3 4 6 8 4 2 2 6 5 9 3 5 0 5 8 6 5 7 9 1 3 5 6 3 4 7 8 1 6 1 488 1 5 9 9 0 0 8 3 8 2 9 9 9 8 5 1 4 5 0 1 5 4 4 2 0 1 0 8 4 5 2 9 1 3 5 7 9 5 5 9 8 7 1 5 5 0 0 7 4 8 7 7 7 9 8 9 8 8 
    0 7 1 4 5 4 6 1 1 0 0 8 2 2 3 8 5 6 3 8 6 9 5 0 1 2 0 7 4 8 8 5 5 0 3 9 8 3 1 5 7 1 450 7 7 8 9 4 6 2 7 8 3 3 6 4 4 0 6 9 4 0 0 0 7 3 2 4 5 7 8 9 5 3 9 3 8 8 4 6 7 8 4 5 0 2 2 8 5 7 4 5 9 5 2 3 4 5 4 0 
    7 3 1 9 3 0 5 8 1 9 7 2 4 1 9 4 6 1 4 3 4 0 9 2 5 1 0 6 0 6 6 3 6 7 5 8 3 3 1 5 5 5 7 407 4 8 2 3 8 1 1 1 8 1 2 1 9 5 2 5 7 4 4 0 7 0 4 2 3 1 3 0 1 7 9 0 0 0 4 7 4 8 8 5 2 4 1 1 9 3 3 6 2 2 8 5 9 5 9 2 
    8 9 3 9 0 1 1 4 6 9 7 3 7 9 2 0 7 6 7 4 1 9 1 6 4 0 7 6 7 0 3 0 1 4 4 2 9 5 5 2 0 9 7 4 452 4 7 9 2 2 0 0 1 6 3 1 8 5 4 5 5 8 9 0 9 6 0 4 0 6 5 9 9 8 1 5 1 7 1 9 0 8 1 3 7 8 5 0 5 5 4 5 1 7 5 4 7 6 8 3 
    8 6 9 2 1 9 1 5 1 4 3 3 6 2 7 3 5 3 8 5 5 9 2 5 0 1 0 9 1 1 7 9 9 7 8 1 6 8 6 6 6 9 8 8 4 482 2 3 7 3 2 7 2 0 5 8 0 1 4 3 1 9 5 7 4 4 9 6 7 5 3 9 7 6 9 3 2 8 4 2 3 8 2 6 3 8 2 5 0 3 3 8 8 7 9 0 1 7 8 5 
    1 6 9 2 6 6 4 7 0 1 5 0 8 9 6 9 7 9 3 1 6 7 6 3 1 1 1 8 9 1 2 8 9 6 2 1 0 4 6 0 8 0 9 2 7 2 485 8 2 2 2 1 1 9 6 8 7 5 5 8 8 6 5 7 8 0 9 0 3 4 6 1 8 7 3 3 5 6 7 2 9 9 3 9 7 8 4 7 3 0 7 3 2 6 7 3 3 6 5 8 
    1 8 9 2 3 9 3 9 6 5 6 9 5 2 1 3 3 0 7 8 2 7 9 0 5 2 9 5 9 7 0 6 9 7 4 4 1 5 7 0 2 0 4 3 9 3 8 433 0 6 8 2 0 3 2 6 3 2 6 3 0 6 7 0 6 8 1 1 4 7 3 2 6 9 4 6 9 6 0 1 5 8 3 1 3 3 3 6 0 4 3 2 1 7 8 6 3 1 4 7 
    9 5 1 6 6 9 8 2 0 1 1 2 1 8 7 9 4 8 0 5 8 5 7 5 2 0 4 2 6 6 7 7 4 0 0 5 1 8 0 1 7 8 6 8 2 7 2 0 435 9 4 3 1 3 3 9 3 5 9 0 2 5 7 6 1 0 9 2 6 0 3 7 5 4 8 9 1 3 9 5 1 2 9 9 5 3 3 1 9 1 3 9 0 1 6 1 3 4 0 5 
    7 8 7 4 9 1 2 3 7 5 6 6 1 4 8 6 5 5 1 1 7 2 7 6 3 1 5 7 9 3 9 6 1 9 8 9 9 9 5 5 0 3 2 1 2 3 2 6 9 458 9 5 3 5 4 5 4 2 0 4 5 6 6 7 9 6 8 4 1 4 2 1 2 2 4 3 9 1 1 5 6 1 3 8 3 5 3 5 7 5 8 4 1 9 4 0 4 0 1 3 
    9 6 8 9 0 6 5 8 5 9 7 7 1 8 2 5 4 2 5 6 9 4 0 9 6 6 2 3 7 9 7 1 9 8 6 5 4 3 0 5 2 8 7 1 0 2 2 8 4 9 483 7 6 7 0 4 4 5 3 2 4 9 3 9 2 9 4 1 3 4 6 5 7 1 9 6 9 9 3 5 1 5 1 0 5 1 7 4 7 2 5 2 3 1 6 3 8 1 9 0 
    7 6 1 0 3 1 2 7 2 5 0 1 6 8 8 5 3 5 1 1 4 2 2 3 8 5 3 5 4 6 2 6 7 9 8 9 2 3 2 2 6 2 8 1 0 7 1 2 3 5 7 442 8 7 4 5 6 8 9 0 8 6 4 0 3 4 4 3 7 6 8 1 3 3 8 8 8 6 3 9 7 5 8 0 1 0 0 9 1 1 4 6 6 3 9 6 4 0 8 3 
    6 5 7 3 1 3 8 5 7 2 4 3 5 9 2 1 6 7 7 5 7 9 6 4 0 5 1 3 5 8 1 3 5 0 5 0 7 6 2 7 3 9 3 8 1 2 1 0 1 3 6 8 447 4 0 9 0 7 6 4 2 6 1 3 2 0 7 1 5 9 0 8 4 0 8 0 1 5 6 6 8 7 7 9 1 0 4 4 9 8 6 6 5 1 6 2 7 7 6 5 
    7 7 7 6 8 2 6 8 8 2 2 7 3 6 6 7 2 5 5 8 4 6 6 9 7 8 8 8 1 9 8 0 2 5 8 6 1 7 4 9 8 9 3 1 6 0 9 3 3 5 7 7 4 507 0 9 6 2 1 3 3 6 2 5 8 3 6 2 9 4 7 8 2 9 6 0 0 7 4 6 5 7 5 0 2 7 0 3 9 5 8 3 6 1 4 1 9 7 3 5 
    3 6 9 1 4 6 7 0 3 5 6 0 2 4 0 1 3 5 2 5 1 6 4 0 5 5 6 8 1 8 5 1 5 9 7 1 8 7 2 4 7 9 6 2 3 5 6 2 3 4 0 4 0 0 387 5 4 9 0 1 5 9 3 6 5 0 3 1 3 7 5 8 0 2 2 0 7 5 4 0 0 5 7 6 1 2 1 6 6 0 2 0 0 8 8 5 3 4 1 2 
    4 0 7 3 7 8 3 5 6 4 0 2 8 9 0 6 6 4 3 8 9 7 4 4 7 1 3 9 4 0 0 4 6 0 8 4 0 6 6 9 7 8 4 1 1 8 8 6 9 5 4 5 9 9 5 503 5 0 5 5 9 8 4 6 7 5 6 7 3 1 1 7 7 4 8 4 3 8 1 0 3 6 3 3 9 6 5 6 4 9 6 9 5 9 4 7 4 6 2 1 
    6 8 0 6 8 9 9 3 4 1 6 9 6 9 1 8 7 4 2 7 0 9 0 1 3 9 7 7 4 2 9 3 9 3 6 6 3 0 8 6 5 5 4 9 8 0 7 3 3 4 4 6 0 6 4 5 486 6 3 1 8 9 9 0 8 8 0 7 1 1 7 3 8 5 6 9 3 6 6 1 5 1 7 4 0 3 8 5 7 1 1 4 3 6 2 3 6 7 5 6 
    8 6 8 2 3 1 8 4 6 7 3 6 5 4 6 2 3 9 3 4 4 9 3 5 1 8 4 3 3 7 9 7 5 5 2 5 7 4 7 7 7 1 0 5 5 1 5 2 5 2 5 8 7 2 9 0 6 518 4 9 4 1 9 8 9 9 9 9 6 8 4 6 4 3 3 8 6 9 4 2 8 9 2 4 9 7 1 8 2 3 2 6 7 7 9 5 1 6 3 2 
    5 9 0 0 4 2 0 4 8 9 3 4 6 2 1 4 9 8 9 9 1 5 6 0 4 1 3 0 5 1 1 4 3 2 9 8 9 4 2 8 9 4 6 2 4 4 5 6 9 0 3 9 6 1 0 5 3 4 421 8 3 2 5 7 6 9 4 4 6 6 1 4 9 8 8 7 1 1 1 0 0 1 2 8 5 8 0 3 4 3 0 4 3 4 8 2 3 0 9 1 
    6 3 4 8 7 1 0 0 6 2 0 5 1 3 7 3 7 1 8 7 8 2 1 0 8 8 8 5 4 6 1 7 0 4 2 4 8 1 6 4 0 5 9 5 5 3 8 3 0 4 2 0 4 3 1 5 1 9 8 394 3 4 9 6 8 0 4 4 5 1 7 2 3 1 3 9 2 2 5 7 1 1 3 4 6 0 2 4 3 7 0 2 6 8 0 8 1 2 4 5 
    1 1 2 8 9 4 0 6 0 7 0 5 4 8 2 2 6 0 0 3 5 5 2 7 8 6 5 5 3 1 9 1 4 1 1 6 2 9 2 0 0 0 4 7 5 1 8 0 2 5 4 8 2 3 5 9 8 4 3 3 408 9 6 5 2 1 2 2 1 4 1 8 8 7 8 7 3 5 1 2 3 9 6 6 3 7 7 2 8 3 0 5 1 0 7 5 5 8 2 5 
    3 3 7 2 2 9 5 1 8 9 3 9 4 6 6 3 1 8 8 3 5 5 8 3 7 0 1 6 0 1 5 9 4 5 0 9 7 3 3 8 4 1 0 4 8 9 6 6 5 6 9 6 6 6 9 8 9 1 2 4 9 516 8 7 2 5 5 8 2 8 3 6 7 7 1 2 5 7 7 1 2 7 8 8 2 9 9 7 4 3 3 8 7 4 9 1 5 3 6 9 
    1 3 7 8 8 0 4 9 1 5 1 1 3 7 3 8 9 1 9 7 3 9 6 6 7 4 8 3 9 1 7 2 1 8 2 4 1 9 9 0 6 5 0 4 9 5 5 7 7 6 3 4 1 2 3 4 9 9 5 9 6 8 499 6 8 9 7 3 3 2 6 5 7 2 2 8 2 3 8 9 0 7 4 7 7 8 5 5 7 3 4 3 2 1 1 3 3 9 4 8 
    6 6 6 3 7 7 8 1 9 8 3 8 1 6 2 3 3 8 3 9 4 9 8 3 5 3 4 7 3 9 0 4 2 4 8 0 1 0 3 2 2 4 0 0 0 7 7 0 6 7 9 0 3 5 6 6 0 8 7 6 5 7 6 463 4 4 6 2 5 3 2 0 1 4 3 9 4 8 5 4 7 4 4 4 5 9 4 1 2 7 8 3 1 6 9 6 8 8 9 7 
    3 0 2 2 9 5 2 8 5 1 9 0 2 7 8 3 6 0 6 0 9 6 5 4 3 4 5 2 4 7 1 2 5 3 3 8 7 8 6 4 4 4 7 7 9 4 8 6 1 9 2 3 2 8 5 7 8 9 6 8 2 2 8 4 477 7 1 3 0 4 6 4 2 0 2 3 6 8 8 7 8 7 0 5 0 5 8 4 3 9 1 7 5 6 9 8 7 4 0 7 
    1 6 2 1 5 8 3 5 5 7 1 4 1 4 2 9 9 3 8 3 2 4 1 0 8 2 3 9 5 8 3 2 9 1 1 6 2 7 6 2 6 2 3 0 6 4 0 8 0 6 9 4 0 3 0 5 8 9 9 0 1 5 9 4 7 402 7 4 3 5 0 3 3 5 4 0 0 9 6 1 3 0 4 8 5 4 4 1 2 7 0 3 0 1 6 3 4 8 9 3 
    1 9 8 2 1 2 5 5 1 5 9 6 3 6 0 3 7 8 0 5 6 6 4 1 2 3 8 0 2 3 8 7 1 5 0 5 3 4 1 9 3 0 2 4 0 9 9 1 9 8 4 4 7 6 3 6 0 9 4 4 2 5 7 6 1 7 447 5 8 9 8 9 2 9 0 1 8 4 6 0 4 7 6 2 6 6 1 4 4 1 3 8 7 2 1 5 9 2 6 2 
    9 1 3 8 6 8 2 3 9 2 7 0 3 9 8 5 7 2 0 7 6 2 5 8 9 2 2 0 4 1 6 0 7 3 6 0 1 4 9 5 0 1 4 2 4 6 0 1 2 4 1 3 1 2 1 7 7 9 4 4 2 8 3 2 3 4 5 414 2 3 6 0 9 5 8 2 6 0 4 2 2 8 5 8 2 6 9 6 7 5 8 4 6 0 0 3 0 4 0 5 
    2 7 3 9 6 2 6 7 9 7 9 4 8 1 6 3 3 9 1 7 4 1 2 1 3 4 1 7 3 2 4 8 7 9 3 6 0 2 1 0 7 0 5 3 0 7 3 4 6 1 3 7 5 9 3 3 1 6 6 5 1 2 3 5 0 3 8 2 450 8 1 1 7 6 3 2 0 7 2 8 4 3 6 8 5 7 7 7 7 3 0 8 9 8 9 4 4 1 7 9 
    4 5 5 9 6 7 7 8 6 9 9 0 0 5 0 3 2 7 7 9 5 8 9 5 1 2 1 0 3 3 3 3 4 7 8 2 7 7 5 4 5 8 7 1 6 5 4 7 0 4 4 6 9 4 7 1 1 8 6 1 4 8 2 3 4 5 9 3 8 489 7 7 1 9 1 6 7 8 0 1 6 8 4 6 8 6 8 2 4 3 2 8 0 0 4 6 8 9 6 8 
    1 8 6 5 6 0 4 8 0 3 1 2 3 5 9 1 0 2 4 2 1 6 7 4 8 7 8 7 3 8 3 6 1 5 2 4 6 8 5 3 5 4 8 3 5 3 6 3 3 2 6 8 0 7 5 1 7 4 1 7 1 3 6 2 6 0 8 6 1 7 419 3 9 5 3 9 4 4 4 7 4 0 8 1 1 3 7 2 5 5 1 9 0 4 2 0 5 3 1 0 
    0 2 9 2 0 4 1 7 6 6 0 6 8 2 3 2 0 5 7 0 5 6 8 4 2 4 1 0 8 5 6 9 7 7 6 0 2 3 3 9 7 5 9 0 9 9 1 2 7 1 5 1 8 8 8 7 3 6 4 2 8 6 5 0 4 3 9 0 1 7 3 474 7 1 6 9 7 6 6 8 3 2 6 6 3 9 4 6 2 5 9 8 9 7 4 5 1 7 2 4 
    7 3 5 2 2 7 6 6 4 8 3 6 8 5 0 3 5 7 3 5 5 6 0 8 6 7 6 4 2 7 9 6 8 3 0 6 7 2 4 9 0 2 5 1 9 7 8 6 5 2 7 3 4 2 0 7 8 4 9 3 8 7 7 1 2 3 2 9 7 1 9 7 457 1 0 7 0 2 1 9 7 8 0 5 1 0 1 0 9 3 1 8 3 0 1 0 5 5 8 9 
    3 0 4 7 8 6 2 7 3 4 3 4 4 2 5 4 9 7 6 5 2 4 6 2 0 4 6 2 9 0 6 3 6 0 9 3 8 9 3 3 5 9 3 7 8 6 7 9 4 2 1 3 0 9 2 4 5 3 8 1 7 7 2 4 0 5 9 5 6 9 5 1 1 459 4 5 2 0 8 8 9 6 1 6 6 0 1 8 5 1 9 3 5 3 0 9 0 2 7 9 
    0 2 0 8 9 4 0 8 4 9 9 2 8 6 5 1 4 2 5 4 6 4 8 7 5 9 9 7 0 8 8 2 0 2 6 3 5 0 2 7 0 1 9 9 1 9 3 4 8 4 9 8 8 6 2 8 6 3 8 3 8 1 2 3 2 4 0 8 3 1 3 6 0 4 472 7 6 7 6 4 3 3 9 5 7 8 5 7 5 2 6 5 3 5 5 4 1 0 9 8 
    2 5 4 3 9 9 0 9 5 8 7 6 3 8 4 6 3 1 5 1 8 4 9 0 6 8 9 4 8 9 6 2 6 9 1 6 7 2 8 6 5 3 3 0 5 3 3 6 9 3 6 8 0 0 0 4 9 8 7 9 7 2 8 9 3 0 1 2 2 6 9 9 7 5 7 485 3 7 5 1 4 1 5 1 4 3 6 5 7 8 4 0 7 1 5 0 5 2 9 6 
    7 1 8 8 4 6 6 5 3 8 5 1 5 5 0 2 2 6 0 7 7 3 9 9 2 0 8 6 7 6 2 6 3 0 1 1 8 9 7 9 9 5 8 0 1 2 5 9 1 9 9 8 1 0 7 3 3 6 1 2 3 5 2 4 6 0 8 6 0 7 4 7 0 2 6 3 468 3 7 8 7 5 8 4 3 4 4 9 7 3 7 9 4 3 8 2 7 5 1 0 
    5 4 2 1 4 1 6 5 5 3 5 0 8 0 6 9 2 8 4 7 9 2 6 8 5 7 2 8 1 6 1 8 7 4 9 6 9 5 8 2 8 7 8 0 7 8 6 6 3 1 9 6 5 7 5 8 6 9 1 2 5 7 3 8 8 9 4 0 7 8 4 6 2 0 7 7 3 486 5 6 3 2 4 8 0 0 4 0 5 6 4 0 0 9 2 1 1 6 4 9 
    8 9 4 2 1 0 2 7 6 8 0 2 0 1 6 4 6 5 4 1 3 2 3 7 5 8 5 3 1 9 6 7 9 2 4 2 9 9 7 3 2 9 4 4 1 4 7 0 9 1 3 3 6 4 4 1 6 4 1 5 1 7 8 5 8 6 6 4 2 0 4 6 1 8 6 5 7 5 460 8 9 2 3 4 2 3 3 6 3 6 9 1 3 5 9 2 6 9 5 7 
    4 1 2 9 9 0 7 1 2 7 1 1 9 0 3 9 1 8 3 2 8 8 7 7 6 7 8 2 0 8 3 9 0 5 2 8 0 4 1 8 7 5 6 7 9 2 2 1 5 5 5 9 6 6 0 0 1 2 0 7 2 1 9 4 7 1 0 2 8 1 7 8 9 8 4 1 8 6 8 413 1 0 1 2 0 6 7 1 1 6 2 0 1 4 2 7 4 4 3 0 
    4 6 9 0 4 9 7 3 4 1 6 5 4 9 6 8 8 4 4 2 6 2 0 9 9 6 8 2 7 0 0 0 5 6 4 3 5 0 1 3 6 5 7 4 0 3 9 5 1 6 1 7 8 5 0 3 5 8 0 1 3 2 0 7 8 3 4 2 4 6 4 3 7 9 3 4 7 3 9 1 440 6 8 6 1 9 5 0 0 3 3 7 5 0 8 4 5 9 1 7 
    1 0 2 1 6 4 0 3 5 3 9 7 6 6 4 0 9 1 1 2 7 0 4 3 9 6 0 1 3 3 2 2 5 5 2 4 6 0 4 0 9 9 8 8 8 8 9 8 2 1 5 5 7 7 5 6 1 9 1 1 9 7 7 4 7 0 7 8 3 8 0 2 8 6 3 1 5 2 2 0 6 409 4 2 6 0 4 1 1 0 6 3 9 1 4 4 5 1 9 0 
    4 0 4 9 8 6 0 2 2 2 1 2 5 5 5 5 3 9 7 7 5 2 3 5 3 6 5 3 9 3 7 7 0 8 2 4 6 3 5 4 1 8 4 8 1 2 3 3 9 3 1 8 7 5 7 3 7 2 2 3 6 8 4 4 0 4 6 5 6 4 8 6 0 1 9 5 8 4 3 1 8 4 454 0 9 1 3 7 9 7 1 4 5 2 4 3 6 9 8 2 
    3 1 8 7 6 9 0 7 4 1 1 9 4 1 9 6 9 4 2 6 2 3 3 3 6 7 9 4 9 6 6 2 0 7 0 4 8 2 2 6 2 7 5 5 3 6 9 1 9 8 0 0 9 0 6 3 4 4 8 4 6 8 7 4 5 8 2 8 8 6 1 6 5 6 5 1 4 8 4 2 6 2 0 461 3 9 5 0 5 0 4 0 1 5 6 6 2 8 0 6 
    1 5 0 5 5 0 0 5 6 4 4 3 1 5 6 3 7 3 2 1 2 1 9 7 4 2 3 7 4 5 6 9 4 7 5 5 8 7 2 5 4 1 0 2 7 3 7 3 5 3 5 1 1 2 1 9 0 9 5 6 3 2 7 5 0 5 6 2 5 8 1 3 1 6 7 4 3 0 2 0 1 6 9 3 414 8 0 5 9 7 4 4 5 5 9 8 5 4 4 0 
    9 8 4 7 5 1 0 4 7 6 1 2 6 1 7 9 4 4 0 2 3 6 8 4 0 8 6 0 0 6 1 4 5 2 6 9 8 3 1 6 1 5 2 4 8 8 8 3 3 5 1 0 0 7 2 6 3 7 8 0 7 9 8 9 5 4 6 6 7 6 3 9 0 0 8 3 4 0 3 6 9 0 1 9 8 451 8 5 5 8 5 2 6 2 1 0 1 5 3 9 
    6 8 5 5 2 8 5 6 1 4 7 2 8 0 9 4 2 0 5 0 6 5 5 3 3 5 1 4 1 2 7 5 9 9 9 4 4 6 3 0 6 5 2 1 5 2 4 3 3 3 7 0 4 0 1 5 8 1 0 2 7 9 5 4 8 4 1 9 7 8 7 4 1 1 5 6 4 4 3 7 5 4 3 5 0 8 446 1 6 8 5 4 5 6 9 8 0 4 8 9 
    1 0 9 2 4 7 2 2 8 5 6 8 8 0 9 0 9 8 6 7 3 0 3 2 5 7 8 2 9 5 7 1 4 2 5 2 9 7 3 5 0 0 8 1 0 5 7 6 1 5 4 9 4 3 6 6 5 8 3 4 2 7 5 1 4 1 4 6 7 2 2 6 0 8 7 5 9 0 6 1 0 1 7 0 5 5 1 438 6 3 2 2 6 7 3 6 7 3 8 2 
    9 7 9 5 7 9 9 6 5 6 7 8 3 3 2 7 1 3 6 0 0 9 1 1 7 8 8 4 6 5 0 1 4 5 4 1 1 3 9 4 6 0 5 9 5 0 3 0 9 7 7 1 9 9 6 4 7 2 4 3 8 4 7 2 3 2 4 7 7 4 5 2 9 5 5 7 7 5 3 1 0 1 9 5 9 5 6 6 473 4 1 4 3 1 2 7 5 0 5 8 
    9 2 1 6 4 4 3 6 9 0 3 4 2 2 1 1 8 5 8 4 4 5 2 5 7 9 4 8 7 6 2 7 9 5 6 4 6 2 2 0 5 7 7 3 5 3 0 4 1 5 2 1 8 5 0 9 1 3 3 7 3 3 3 7 9 7 1 5 3 3 5 5 3 1 2 8 3 6 6 6 3 0 7 0 7 8 8 3 4 442 1 4 5 6 4 4 7 8 5 4 
    5 7 3 3 9 5 2 4 3 1 1 5 9 5 7 6 8 0 1 2 1 9 8 3 7 6 9 2 0 0 0 5 4 7 9 3 8 4 9 6 7 4 4 3 4 3 7 3 3 8 5 4 6 8 2 6 1 2 0 0 0 3 4 8 1 0 3 8 0 2 1 9 1 9 6 4 7 4 9 2 3 6 1 4 4 5 5 2 1 1 422 4 1 4 4 3 5 6 7 6 
    8 9 9 6 6 3 2 2 1 6 6 6 5 8 4 9 8 7 1 7 4 2 0 9 9 1 6 1 5 9 1 6 1 9 1 9 5 2 0 5 4 8 5 6 5 8 3 2 9 4 2 6 6 3 0 9 4 6 4 2 5 8 3 3 7 3 8 4 8 8 9 8 8 3 5 0 9 0 1 0 7 3 4 0 4 2 4 2 4 4 4 488 9 6 9 1 1 6 8 9 
    9 6 1 3 8 5 4 2 3 3 6 7 9 5 1 2 9 4 4 2 5 1 9 5 7 0 0 6 9 9 3 2 8 3 0 6 2 8 4 4 8 7 9 2 1 8 2 1 0 1 3 6 5 6 0 5 3 7 3 6 1 7 2 1 5 0 7 6 9 0 0 9 3 5 3 7 4 0 3 1 5 9 5 1 5 6 5 6 3 5 1 9 443 3 6 8 1 9 6 8 
    4 8 5 4 0 7 4 7 5 8 0 2 5 4 0 8 5 4 0 3 9 2 0 8 1 5 0 1 1 7 9 5 5 6 1 9 6 2 1 4 8 7 5 2 7 7 6 7 1 9 1 3 1 1 8 9 6 7 4 8 0 4 1 6 6 1 2 0 8 0 4 7 0 3 5 1 3 9 5 4 0 1 2 5 5 2 6 7 1 6 4 6 3 420 9 3 2 6 7 1 
    1 7 8 6 4 6 8 4 9 8 6 9 5 8 5 1 6 5 0 3 8 1 5 0 7 0 4 0 7 2 7 8 7 6 6 7 4 4 4 0 0 7 2 8 5 9 7 8 6 4 6 9 6 4 8 4 2 9 8 0 7 9 1 9 9 6 1 0 9 4 2 4 1 0 5 5 8 2 9 2 8 4 4 6 9 1 9 3 2 4 4 9 6 9 509 7 8 0 7 0 
    8 2 8 2 6 8 8 2 3 5 5 2 1 6 9 6 6 5 1 8 2 2 8 0 0 8 1 4 1 1 5 9 3 9 5 4 1 8 1 0 8 9 3 5 4 0 3 6 1 0 3 6 2 1 5 7 3 5 2 8 5 1 3 6 8 3 5 3 4 6 0 5 0 9 4 0 2 1 2 7 4 4 3 6 8 0 8 6 7 4 3 1 8 3 7 415 3 1 7 4 
    8 1 7 5 0 9 1 0 8 7 3 8 4 8 0 8 9 4 4 2 9 2 7 2 3 0 0 1 3 7 3 4 1 8 6 9 3 1 2 1 8 8 4 9 7 1 3 3 3 4 8 4 7 9 3 4 6 1 3 1 5 5 3 8 7 4 9 0 4 8 5 1 5 0 1 5 7 1 6 4 5 5 6 2 5 1 0 7 5 7 5 1 1 2 8 3 430 3 5 5 
    2 0 3 2 3 0 6 1 9 1 3 1 2 4 9 3 9 5 4 2 5 5 0 2 9 0 8 0 1 0 3 9 5 1 4 9 8 3 2 9 1 9 5 5 6 7 6 1 4 0 1 0 7 7 4 6 7 6 0 2 8 3 9 8 4 8 2 4 1 9 3 7 5 2 0 2 5 6 9 4 9 1 9 8 4 5 4 3 0 8 6 6 9 6 0 1 3 432 9 4 
    7 1 8 3 8 7 1 5 8 1 8 3 5 3 5 3 4 5 3 2 4 8 3 7 9 7 9 5 5 0 5 2 3 3 1 2 1 2 2 0 9 8 4 9 8 8 5 4 0 1 9 8 6 3 1 2 5 3 9 4 2 6 4 9 0 9 6 0 7 6 1 2 8 7 9 9 1 4 5 3 1 9 8 0 4 3 8 8 5 5 7 8 6 7 7 7 5 9 494 8 
    4 3 2 2 0 6 1 8 1 3 0 0 6 7 2 9 3 4 2 9 1 9 1 9 9 1 2 0 8 6 2 9 4 9 1 4 3 2 6 3 6 8 0 2 3 5 8 7 5 3 0 3 5 5 2 1 6 2 1 5 5 9 8 7 7 3 2 5 9 8 0 4 9 9 8 6 0 9 7 0 7 0 2 6 0 9 9 2 8 4 6 9 8 1 0 4 5 4 8 446 

    Inverse Power Method finds smallest eigenvalue
    0.002165947796443061


**Last Modified:** December/2021

[Back](../README.md)
