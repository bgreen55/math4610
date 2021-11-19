# task 3 in tasksheet 7 of math 4610
from random import randint

# this function creates a square matrix of size n with random numbers from 0-10
def randSqrMatrix(n):
    A = []

    for i in range(n):
        x = []
        for j in range(n):
            value = randint(0, 10)
            x.append(value)
        A.append(x)

    #print the matrix
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print()
    print()

    return A


def randUpperTMatrix(n):
    A = []

    for i in range(n):
        x = []
        for j in range(n):
            if j > i:
                value = randint(0, 10)
                x.append(value)
            elif j == i:
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


def randLowerTMatrix(n):
    A = []

    for i in range(n):
        x = []
        for j in range(n):
            if j < i:
                value = randint(0, 10)
                x.append(value)
            elif j == i:
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


def diagDomMatrix(n):
    A = []

    for i in range(n):
        x = []
        for j in range(n):
            if j == i:
                value = randint(0, 8)
                x.append(value)
            else:
                value = randint(0, 8)
                x.append(value)

        A.append(x)

    # make the diagonal entry of the matrix greater than the sum of the other entries in the row
    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j:
                sum = sum + A[i][j]

        if A[i][i] <= sum:
            value = randint(sum, sum + 10)
            A[i][i] = value


    # print the matrix
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print()
    print()



def main():
    randSqrMatrix(3)
    randUpperTMatrix(4)
    randLowerTMatrix(4)
    diagDomMatrix(3)

main()
