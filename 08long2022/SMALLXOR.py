# https://www.codechef.com/submit/SMALLXOR

# Sort the numbers in O(n)log(n), perform xor operations by iteration of the array until a newly created xored-value is the new minimum element.
# The remaining operations will xor this number solely.


for t in range(int(input())):

    n,x,y = [int(el) for el in input().split()]
    a = sorted([int(el) for el in input().split()])

    new = []
    currentmin = (float('inf'),-1)
    for index, el in enumerate(a):

        if el < currentmin[0] and y != 0:
            el ^= x
            new.append(el)
            currentmin = min((el,index), currentmin)
            y -= 1
        else:
            index -= 1
            break

    newarray = new + a[index+1::]

    if y%2 != 0:
        newarray[currentmin[1]] ^= x

    print(*sorted(newarray))