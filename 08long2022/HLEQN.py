# https://www.codechef.com/submit/HLEQN

# the expression can be rewritten as (a+2)(b+2) = x+4
# this shows that x+4 cannot be a prime or a prime*2

import math

def solve(x):

    x += 4

    if not any(x%el == 0 for el in range(2, int(math.sqrt(x)) + 1)):
        return 'NO'

    if x%2 == 0:
        x //= 2
        if not any(x % el == 0 for el in range(2, int(math.sqrt(x)) + 1)):
            return 'NO'

    return 'YES'


def driver():

    tests = int(input())
    for test in range(tests):
        x = int(input())
        print(solve(x))

driver()