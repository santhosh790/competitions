def get_different_number(arr):
    if len(arr) == 1:
        if arr[0] == 0:
            return 1
        else:
            return 0

    for i in range(len(arr)):
        if abs(int(arr[i])) < len(arr):
            arr[abs(int(arr[i]))] = '-'+str(arr[abs(int(arr[i]))])
    print(arr)
    for i in range(len(arr)):
        if arr[i] != '-0' and int(arr[i]) > 0:
            return i
    return (i+1)


'''
non negative not sorted no duplicates
1 3 4 5 ans = 0
0 2 4 ans = 1
0 2 3 ans = 1
0 1 2 4 ans = 3
5 0 3 2 ans = 1

nlogn 1
n n
n 1

5 0 3 2  
0 1 2 3
-1 0 -1  -1
5 0 3 2
0 1 2 3

-5 0 -3 -2

-2 -3 -6 -4 -1 0

-2 -3 -6 -5 1 -0 - 4 
'''
