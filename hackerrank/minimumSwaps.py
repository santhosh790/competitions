#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    '''
    i = 1
    #first = a[0]
    length = len(arr)
    swaps = 0
    for i in range(length):
        for j in range(length):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swaps = swaps + 1
    print(arr)
    return swaps
    '''
    ## The problem clearly says, the numbers are consecutive and unordered.
    ## Logic: Check if the number is in it's designated index.
    ## 1 should be at the position 0, 2 at 1, 3 at 2, etc.,
    ## if not, find the position of the number and swap it. Do for all elements. 
    counter = 0
    for i in range(len(arr)):
        if (arr[i]) != i+1:
                l = arr.index(i+1)
                print(l)
                arr[i],arr[l] = i+1,arr[i]
                counter += 1
        print(arr)
    return counter

print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))

'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
'''