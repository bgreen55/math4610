
**Routine Name:**           partialPivotingOnHilbertMartices

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 main.py


**Description/Purpose:** This routine uses partial pivoting in gaussian elimination to see how well it can approximate solutions to linear systems that consist 
of Hilbert matrices.  The routine also uses the method matrixMultVector to multiply a matix and a vector together.

**Input:**  The routine needs to be given a size for how big the hilbert matrix is going to be.  The method GEAndBackSubScaledPivot must be imported to run this routine. 
However it is included in the following code example. 

**Output:** This routine multiplies a hilbert matrix with a vector of ones which returns a vector we called b.  It then uses LU factorization to return 
the vector x in the Linear system Ax=b.  The closer the vector x is to being all ones the better.  

**Usage/Example:**


The code shows the following example.  This routine multiplies a hilbert matrix with a vector of ones which returns a vector we called b.  
It then uses partial pivoting in gaussian elimination to return the vector x in the Linear system Ax=b.  The closer the vector x is to being all ones the better.  
The code goes through this process will hilbert matrices from size 4 to size 10. 



**Implementation/Code:** The following is the code for main(). 

    
    def hilbertMatrix(n):
        A = []
        for i in range(n):
            a = []
            for j in range(n):
                a.append(None)
            A.append(a)


        for i in range(1, n + 1):
            for j in range(1, n + 1):
                A[i - 1][j - 1] = 1 / (i + j - 1)

        return A


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


    def matrixMultVector(A, x):
        n = len(x)
        b = [0] * n

        for i in range(n):
            for j in range(n):
                b[i] = b[i] + A[i][j] * x[i]

        return b


    def main():
        print("Hilbert Matrix n = 4")
        A = hilbertMatrix(4)
        y = [1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = GEAndBackSubScaledPivot(A, b)
        print(x)

        print("\nHilbert Matrix n = 5")
        A = hilbertMatrix(5)
        y = [1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = GEAndBackSubScaledPivot(A, b)
        print(x)

        print("\nHilbert Matrix n = 6")
        A = hilbertMatrix(6)
        y = [1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = GEAndBackSubScaledPivot(A, b)
        print(x)

        print("\nHilbert Matrix n = 7")
        A = hilbertMatrix(7)
        y = [1, 1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = GEAndBackSubScaledPivot(A, b)
        print(x)

        print("\nHilbert Matrix n = 8")
        A = hilbertMatrix(8)
        y = [1, 1, 1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = GEAndBackSubScaledPivot(A, b)
        print(x)

        print("\nHilbert Matrix n = 9")
        A = hilbertMatrix(9)
        y = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = GEAndBackSubScaledPivot(A, b)
        print(x)

        print("\nHilbert Matrix n = 10")
        A = hilbertMatrix(10)
        y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = GEAndBackSubScaledPivot(A, b)
        print(x)


    main()

   


Running this routine, the following output was returned. 

    Hilbert Matrix n = 4
    [0.9999999999999758, 1.000000000000269, 0.999999999999351, 1.0000000000004226]

    Hilbert Matrix n = 5
    [0.9999999999999198, 1.0000000000013667, 0.9999999999944567, 1.0000000000079992, 0.9999999999962228]

    Hilbert Matrix n = 6
    [0.9999999999991266, 1.0000000000245015, 0.9999999998359812, 1.0000000004235585, 0.9999999995349267, 1.0000000001825244]

    Hilbert Matrix n = 7
    [0.9999999999940888, 1.0000000002330263, 0.999999997773074, 1.000000008608076, 0.9999999842864737, 1.000000013532829, 0.9999999955684493]

    Hilbert Matrix n = 8
    [0.9999999999625995, 1.0000000020372684, 0.999999973104976, 1.0000001467149675, 0.9999996025837361, 1.000000565064629, 0.9999995962784046, 1.000000114282885]

    Hilbert Matrix n = 9
    [0.999999999701814, 1.0000000204203794, 0.9999996562221409, 1.0000024444023528, 0.999991061506811, 1.0000182065747645, 0.9999791317722965, 1.00001258420472, 0.9999968949940096]

    Hilbert Matrix n = 10
    [0.999999999368646, 1.0000000541483118, 0.9999988534555176, 1.000010372818601, 0.9999507243641406, 1.000134990129371, 0.9997791835772913, 1.0002128374822519, 0.9998885185737293, 1.0000244664942262]



I believe these results to be satisfactory, because we were able to get extremely close to 1 for each entry, and as the size of the matrix goes up 
it doesn't appear that we lose much accuarcy.  

**Last Modified:** November/2021

[Back](../README.md)
