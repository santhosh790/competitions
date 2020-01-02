#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cl = len(c)
    i = 0
    firstC = 0
    maximumStep = 2
    maxStep = 2
    for i in range(len(c)):
        if c[i] == 0:
            firstC = i
            break
    jump = 0
    while firstC < cl:
        '''
        ## This is a specific one when maxStep is 2
        if firstC+maxStep < cl and c[firstC+maxStep] == 0:
            print(jump)
            jump = jump+1
            firstC = firstC+maxStep
        elif firstC+1 < cl and c[firstC+1]==0:
            jump = jump + 1
            firstC = firstC+1
        else:
            firstC = firstC+1
        '''
        # This code block is when maxStep is generic
        maxStep = maximumStep
        jumped = False
        while maxStep >= 1:
            #print("c step"+str(maxStep))
            if firstC+maxStep < cl and c[firstC+maxStep] == 0:
                print("jump"+str(jump))
                jump = jump + 1
                jumped = True
                firstC = firstC+maxStep
                break
            maxStep = maxStep - 1
        if not jumped:
            firstC = firstC + 1
        '''
        print(str(firstC))
        print("Next step"+str(jump))
        '''
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
