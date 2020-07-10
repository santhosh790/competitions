'''
In this question we’ll implement a function root that calculates the n’th root of a number. The function takes a
nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of
0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

'''



def root(x, n):
    if x==0:
        return 0
    low = 0
    high = max(1.0, x)
    rootVal = float((high+low)/2)

    while (rootVal - low) >= 0.001:
        if rootVal**n > x:
            high = rootVal
        elif rootVal**n < x:
            low = rootVal
        else:
            break
        rootVal = (high+low)/2
    return rootVal



