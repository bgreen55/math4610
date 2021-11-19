# task 4 for tasksheet 7 of math 4610
from random import randint


def diagonalMatrix(n):
    A = []

    for i in range(n):
        x = []
        for j in range(n):
            if i == j:
                value = randint(1, 10)
                x.append(value)
            else:
                x.append(0)
        A.append(x)

    # print the matrix
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print()
    print()


def main():
    diagonalMatrix(5)


main()
