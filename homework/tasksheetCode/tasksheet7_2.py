# task 2 of tasksheet 7 math 4610
import task1

# this function transposes a matrix
def transposeMatrix(A):
    n = len(A)
    x = []

    # create empty transposed matrix as x
    for i in range(n):
        a = []
        for j in range(n):
            a.append(None)
        x.append(a)

    # take values from A and put them in the transposed matrix
    for i in range(n):
        for j in range(n):
            x[j][i] = A[i][j]

    #print out transposed matrix
    for i in range(n):
        for j in range(n):
            print(x[i][j], end=" ")
        print()

    print()

    return x


# this function takes A and b in Ax = b and returns x.  The fucntion preforms forwards substitution to solve lower triangular matrix
def forwardSub(A, b):
    n = len(A)
    y = [None] * n

    for i in range(0, n):
        sum = b[i]
        for j in range(0, i):
            sum = sum - (A[i][j] * y[j])

        y[i] = sum / A[i][i]

    return y


def main():
    print("Task 2")
    A, b = task1.matrixInit(4)

    x = transposeMatrix(A)
    y = forwardSub(x, b)

    print(y)


main()
