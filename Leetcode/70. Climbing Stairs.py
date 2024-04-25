def climbStairs(n):
    for _ in range(1,n):
        a = 1
        b = a
        c = a+b
        return c



print(climbStairs(3)) # output: 3