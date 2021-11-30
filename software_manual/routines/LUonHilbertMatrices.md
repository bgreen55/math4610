
**Routine Name:**           LUfactorOnHilbertMartices

**Author:** Bradley Green

**Language:** Python. The code was built using Pycharm. Can be run in terminal by:


    python3 main.py


**Description/Purpose:** This routine uses LU factorization, to see how well it can approximate solutions to linear systems that consist of Hilbert matrices.

**Input:**  The routine needs to be given a size for how big the hilbert matrix is going to be.  The method LUfactor must be imported to run this routine. 

**Output:** This routine multiplies a hilbert matrix with a vector of ones which returns a vector we called b.  It then uses LU factorization to return 
the vector x in the Linear system Ax=b.  The closer the vector x is to being all ones the better.  

**Usage/Example:**


The code shows the following example.  This routine multiplies a hilbert matrix with a vector of ones which returns a vector we called b.  
It then uses LU factorization to return the vector x in the Linear system Ax=b.  The closer the vector x is to being all ones the better.  The code
goes through this process will hilbert matrices from size 4 to size 10. 



**Implementation/Code:** The following is the code for main().  The method LUfactor must be imported to run this routine. 

    
    from task2 import LUfactor


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


    def matrixMultVector(A, x):
        n = len(x)
        b = [0] * n

        for i in range(n):
            for j in range(n):
                b[i] = b[i] + A[i][j] * x[i]

        return b


    # the closer the x vector is to all 1 the better
    def main():
        print("Hilbert Matrix n = 4")
        A = hilbertMatrix(4)
        y = [1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = LUfactor(A, b)
        print(x)

        print("\nHilbert Matrix n = 5")
        A = hilbertMatrix(5)
        y = [1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = LUfactor(A, b)
        print(x)

        print("\nHilbert Matrix n = 6")
        A = hilbertMatrix(6)
        y = [1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = LUfactor(A, b)
        print(x)

        print("\nHilbert Matrix n = 7")
        A = hilbertMatrix(7)
        y = [1, 1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = LUfactor(A, b)
        print(x)

        print("\nHilbert Matrix n = 8")
        A = hilbertMatrix(8)
        y = [1, 1, 1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = LUfactor(A, b)
        print(x)

        print("\nHilbert Matrix n = 9")
        A = hilbertMatrix(9)
        y = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = LUfactor(A, b)
        print(x)

        print("\nHilbert Matrix n = 10")
        A = hilbertMatrix(10)
        y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        b = matrixMultVector(A, y)
        x = LUfactor(A, b)
        print(x)


    main()
        
   


Running this routine, the following output was returned. 

    
    Hilbert Matrix n = 4
    [0.9999999999999775, 1.0000000000002485, 0.999999999999402, 1.0000000000003886]

    Hilbert Matrix n = 5
    [0.9999999999999655, 1.0000000000005238, 0.9999999999980628, 1.0000000000025913, 0.9999999999988525]

    Hilbert Matrix n = 6
    [0.999999999999228, 1.000000000021937, 0.9999999998517923, 1.0000000003853693, 0.999999999574584, 1.00000000016768]

    Hilbert Matrix n = 7
    [0.9999999999944524, 1.0000000002215987, 0.9999999978643687, 1.0000000083033338, 0.9999999847780691, 1.0000000131521882, 0.9999999956820236]

    Hilbert Matrix n = 8
    [0.9999999999662691, 1.00000000180906, 0.9999999763726758, 1.0000001278681026, 0.9999996557641158, 1.0000004870421637, 0.9999996534271247, 1.0000000977747472]

    Hilbert Matrix n = 9
    [0.9999999997602121, 1.0000000164521592, 0.9999997226859642, 1.0000019734507875, 0.9999927795056808, 1.0000147132093888, 0.9999831308861128, 1.0000101748012682, 0.9999974890861828]

    Hilbert Matrix n = 10
    [0.9999999987548338, 1.0000001067849733, 0.9999977378614773, 1.0000204794185086, 0.9999026418473493, 1.0002669070133299, 0.9995630884702723, 1.0004214011575985, 0.9997791407962119, 1.0000484987218523]

I believe these results to be satisfactory, because we were able to get extremely close to 1 for each entry, and as the size of the matrix goes up 
it doesn't appear that we lose much accuarcy. 

**Last Modified:** November/2021

[Back](../README.md)
