import math

def matrix():

    be = [[12, 13, 8], [2, 1, 87], [16, 6, 4]]

    return be


b = matrix()

print("b[1][2] =", b[1][2])

def rounded():

    n = 0.3
    y = 0.45

    x = (n+y)*5
    k = math.floor((n+y)*5)

    return x, k

x, k = rounded()

print(x, k)


