import math
count = int(input())
for each in range(count):
    inputVal = int(input())
    val = math.log(inputVal)/math.log(2)
    if int(val) - val == 0:
        print(int(inputVal))
    else:
        print(int(math.pow(2, int(val)+1)))