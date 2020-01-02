#!/bin/python3

import math
import os
import random
import re
import sys

def isHrGlsAt(rowIn, colindex, arr):
    rows = len(arr)
    cols = len(arr[0])
    return colindex+2 < cols and rowIn+2 < rows

def returnHrGlsAt(rowin, colindex, arr):
    values = arr[rowin][colindex:colindex+3]
    values.append(arr[rowin+1][colindex+1])
    values = values+(arr[rowin+2][colindex:colindex+3])
    sum = 0
    for each in values:
        sum = sum + each
    return sum
	
	
# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxVal = -9 * 7
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if isHrGlsAt(i,j,arr):
                sum = returnHrGlsAt(i,j,arr)
                if sum > maxVal:
                   maxVal =  sum
    
    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
