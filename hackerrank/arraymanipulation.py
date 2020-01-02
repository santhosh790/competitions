#!/bin/python3

import math
import os
import random
import re
import sys

# This function is having three different solutions based on the run time
# All the solutions give correct output. The one uncommneted is having better run time complexity
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    print(n)
    print(queries)
    '''
    arr = [0]*n
    maxVal = queries[0][2]
    for each in queries:
        start = each[0] - 1
        end = each[1]
        val = each[2]
        if start < n and end <= n:
            for i in range(start,end):
                print(i)
                arr[i] = arr[i]+val
                if arr[i] > maxVal:
                    maxVal = arr[i]
        print(arr)
    print(arr)
    return maxVal
    '''
    '''
    arr = [0]*(n+2)
    maxVal = queries[0][2]
    for each in queries:
        start = each[0] 
        end = each[1]+1
        val = each[2]
        if start < n+1 and end <= n+1:
            arr[start] = arr[start]+ val
            arr[end] = arr[end]-val
    print(arr)
    max = -sys.maxsize - 1
    #sum = 0
    for i in range(1, len(arr)-1):
        arr[i] = arr[i]+arr[i-1]
        #sum = sum + arr[i]
        if max < arr[i]:
            max = arr[i]
    print(arr)
    return max
    '''
    arr = [0]*(n+2)
    maxVal = queries[0][2]
    for each in queries:
        start = each[0] 
        end = each[1]+1
        val = each[2]
        if start < n+1 and end <= n+1:
            arr[start] = arr[start]+ val
            arr[end] = arr[end]-val
    max = -sys.maxsize - 1
    sum = 0
    for i in range(1, len(arr)-1):
        #arr[i] = arr[i]+arr[i-1]
        sum = sum + arr[i]
        if max < sum:
            max = sum
    return max
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
