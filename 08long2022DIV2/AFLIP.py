# https://www.codechef.com/AUG221B/problems/AFLIP

# Numbers can be exchanged like pieces moving over diagonals in a game like Checkers
# Divide both matrices into two accordingly and collect and compare

from collections import defaultdict

def solve(matrix1, matrix2, n, m):

    # bordercases, no swap possible on if there is one row or one column
    if n == 1 or m == 1 and matrix1 != matrix2:
        return 'NO'

    matrix1a = defaultdict(int)
    matrix1b = defaultdict(int)
    matrix2a = defaultdict(int)
    matrix2b = defaultdict(int)

    index = 0
    for row in range(n):
        for col in range(index,m,2):
            matrix1a[matrix1[row][col]] += 1
            matrix2a[matrix2[row][col]] += 1
        index ^= 1

    index = 1
    for row in range(n):
        for col in range(index,m,2):
            matrix1b[matrix1[row][col]] += 1
            matrix2b[matrix2[row][col]] += 1
        index ^= 1

    if matrix1a == matrix2a and matrix2b == matrix1b:
        return 'YES'
    return 'NO'


def driver():

    tests = int(input())
    for test in range(tests):
        n,m = [int(el) for el in input().split()]
        matrix1 = [input().split() for row in range(n)]
        matrix2 = [input().split() for row in range(n)]
        print(solve(matrix1, matrix2, n, m))

driver()