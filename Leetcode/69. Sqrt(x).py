#  your task is to implement int sqrt(int x).
#  Compute and return the square root of x, where x is guaranteed to be a non-negative integer.


def mySqrt(x):
    return int(x ** 0.5)


print(mySqrt(3)) # output: 1, real sqrt: 1.7320508075688772
print(mySqrt(4)) # output: 2, real sqrt: 2.0
print(mySqrt(8)) # output: 2, real sqrt: 2.8284271247461903

