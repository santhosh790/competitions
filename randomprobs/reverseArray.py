#
#reverse array in place
#

def reverseArray(a):
    end = len(a)-1
    start = 0
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    return a

print(reverseArray([1,2,3,4,5]))