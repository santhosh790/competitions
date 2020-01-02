#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    if 'a' not in s:
        return 0
    if n < len(s):
        return s[:n].count('a')
    noOfRpts = n//len(s)
    subStrSize = n%len(s)
    return s.count('a')*noOfRpts + s[:subStrSize].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
