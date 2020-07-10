'''
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B

'''

def arr2Dcolor(arr, oldc, newc, i, j):
    if i<0 or i>=len(arr):
        return
    if j<0 or j>=len(arr[0]):
        return
    if arr[i][j] == oldc:
        arr[i][j] = newc
        arr2Dcolor(arr, oldc, newc, i+1, j)
        arr2Dcolor(arr, oldc, newc, i-1, j)
        arr2Dcolor(arr, oldc, newc, i, j+1)
        arr2Dcolor(arr, oldc, newc, i, j-1)
    else:
        return
    return arr


arr = [[1,1,1],[0,1,0],[0,0,1]]
arr2Dcolor(arr,1,2,2,2)
print(arr)