#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:]+a[:d]
	
	# Algorithm to calculate new index and update new array for each index (i):
  # new_index = (i + no_of_left_rotation) % length_of_array
  # new_arr[i] = array[new_index]
  #for(int i = 0; i < lengthOfArray; i++){
  #  int newLocation = (i + (lengthOfArray - shiftAmount)) % lengthOfArray;
  #  a[newLocation] = in.nextInt();}

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
