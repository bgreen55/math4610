This page shows the code I ran to complete task 5 in tasksheet 9. It is important to notice that I import two routines to complete the code.  Those routines
 can be found in the software manual page.  


    from random import randint

    from task4 import jacobiIteration
    from task2 import errorL2

    def GEwithBackSub(A, b):
        n = len(b)

        # gaussian elimination
        for k in range(0, n, 1):
            for i in range(k + 1, n, 1):
                factor = A[i][k] / A[k][k]
                for j in range(k, n, 1):
                    A[i][j] = A[i][j] - factor * A[k][j]
                b[i] = b[i] - factor * b[k]


        x = backSub(A, b)

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


    def backSub(A, b):
        n = len(b)
        x = [None] * n
        m = n - 1
        x[m] = b[m] / A[m][m]
        for i in range(m - 1, -1, -1):
            sum = b[i]
            for j in range(i + 1, n, 1):
                sum = sum - A[i][j] * x[j]
            x[i] = sum / A[i][i]

        return x


    def main():
        # random daigonal dominant martix of size 3x3
        print("The random diagonal dominant matrix")
        A = diagSymMatrix(100)
        B = A.copy()
        print("The column vector b")
        b = [1] * 100
        print(b)

        x = [1.1] * 100
        print("\n Solution for JI")
        tt = jacobiIteration(B, b, x, .0001, 100)
        print(tt)


        print("\nSolution fo GE")
        p = GEwithBackSub(A, b)
        print(p)

        print("\n The error between the vectors")
        print(errorL2(tt, p))

    main()
    
 
* Last modified December 2021 *
* [Back](README.md)
    
