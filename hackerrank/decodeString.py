#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decodeString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER numberOfRows
#  2. STRING encodedString
#

def decodeString(numberOfRows, encodedString):
    # Write your code here
    nRows = 3
	value = "mnei_ya_s__m"
	#nRows=2
	#value = "hlowrd_el_ol"
	rowLength = len(value)//nRows
	#for each in range(nRows):
	#    print(each)
	final = ""
	for i in range(rowLength):
		for each in range(nRows):
			print(str(i+(each*rowLength)+each))
			if i+(each*rowLength)+each < len(value):
				final = final + value[i+(each*rowLength)+each]
	print(final)

    
 
    return newVal
if __name__ == '__main__':
