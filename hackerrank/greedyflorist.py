#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    '''
    count = 0
    total = 0
    val = 1
    per = 0
    while(count<len(c)):
        if per == k:
            val += 1
            per = 1
        print(val)
        total = total + (val * c[count])
        count += 1
        per +=1
    return total
    '''
    ## More Easier using arithmatic operation
    t=0
    for i in range(len(c)):
        #print(int(i/k))
        t=t+(int(i/k)+1)*c[i]
    return t
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
