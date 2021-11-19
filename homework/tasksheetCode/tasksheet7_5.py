# task 5 of tasksheet 7 for math 4610
import task3

# this method takes a square matrix A and puts it into row echelon form
def toRowEchelonForm(A, b):
    n = len(b)
    s = [None] * n

    for i in range(0, n, 1):
        s[i] = abs(A[i][0])
        for j in range(0, n, 1):
            temp1 = abs(A[i][j])
            if temp1 > s[i]:
                s[i] = temp1

    for k in range(0, n -1, 1):
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

        for j in range(0, n , 1):
            temp1 = A[k][j]
            A[k][j] = A[q][j]
            A[q][j] = temp1

        for i in range(k+1, n, 1):
            factor = A[i][k] / A[k][k]
            for j in range(k, n, 1):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]

    return A, b


def main():
    # create a random square matrix
    A = task3.randSqrMatrix(3)

    #A = [[1, 1, 1], [1, 2, 2], [1, 3, 5]]
    b = [1, 4, 5]

    # do transformations on A and b to put A in upper row echelon form
    result1, result2 = toRowEchelonForm(A, b)

    print(result1)
    print()
    print(result2)


main()
