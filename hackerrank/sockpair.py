#!/bin/python3

import math
import os
import random
import re
import sys

def pairCalc(sock, pairlist):
    if sock in pairlist:
        pairlist.remove(sock)
        return 1
    else:
        pairlist.append(sock)
        return 0

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    val = 0
    pairs = []
    for i in range(len(ar)):
        val = val + pairCalc(ar[i], pairs)
    return val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
