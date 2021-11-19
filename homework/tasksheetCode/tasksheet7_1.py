# task 1 of task sheet 7 for math 4610

# this function initializes an upper triangular matrix
def matrixInit(n):
    matrixA = []
    matrixb = []

    for i in range(n):
        a = []
        for j in range(n):
            if j < i:
                a.append(0)
            else:
                a.append(i + j - 1)
        matrixA.append(a)

    for i in range(n):
        matrixb.append(1)

    # print the matrix
#    for i in range(n):
#        for j in range(n):
#            print(matrixA[i][j], end=" ")
#        print()

    print()
    return matrixA, matrixb


# this function preforms back substitution on an upper triangular matrix to solve for x in Ax=b
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
    print("Task 1\n")
    # get matrix A of size nxn and a nx1 vector b of all 1
    A, b = matrixInit(3)
    # preform backsubstitution on on A to solve for x in Ax = b
    solution = backSub(A, b)
    print(solution)


main()
