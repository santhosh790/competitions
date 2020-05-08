'''
This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0],
and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

'''
## There is a DP solution for the same problem. Need to understand the same.
## http://anothercasualcoder.blogspot.com/2019/01/max-number-of-coins-by-zillow.html
## https://codezen.codingninjas.com/practice/165764/4997/interview-shuriken-29:-maximum-number-of-coins
def findmax(matmax, i, j):
    if i == len(matmax) or j == len(matmax[0]):
        return 0
    #print(matmax[i][j])
    findmax(matmax, i, j+1)
    return max(matmax[i][j] + findmax(matmax, i + 1, j), matmax[i][j] + findmax(matmax, i, j + 1))

mat = [[0,3 ,1, 1],[2, 0, 0, 4],[1, 5, 3, 1]]
#mat = [[0,1 ,2, 3],[4, 5, 6, 7],[8, 9, 10, 11]]
print(mat)
val = findmax(mat,0,0)
print("Final Val", val)