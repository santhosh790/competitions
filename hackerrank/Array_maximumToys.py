#!/bin/python3

import math
import os
import random
import re
import sys

## 2 approaches are discussed

# Complete the maximumToys function below.
def maximumToys(prices, k):
    '''
    #print
    for i in range(len(prices)):
        for j in range(0, len(prices)-1):
            if prices[j]>prices[j+1]:
                temp = prices[j]
                prices[j] =prices[j+1]
                prices[j+1] = temp
    #'''
    # Here, we iterate over the prices and check if k is matching
    prices.sort() 
    sum = 0
    maxToys = []
    for each in prices:
        sum = sum+each
        if sum <= k:
            maxToys.append(each)
        else: ## Once sum becomes higher than k, it is unncessary to iterate over
            break
    return len(maxToys)
    '''
    prices.sort()
    i = 0
    # Here, we iterated over the amount in hand. earlier prices
    while k > 0 and i < len(prices):
        k -= prices[i]
        i += 1
    return i-1
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
