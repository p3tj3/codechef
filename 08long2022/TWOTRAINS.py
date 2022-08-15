# https://www.codechef.com/submit/TWOTRAINS

# the largest number in the sequence is a bottleneck that has to be doubled

for t in range(int(input())):
    input()
    a = [int(el) for el in input().split()]
    print(sum(a)+max(a))