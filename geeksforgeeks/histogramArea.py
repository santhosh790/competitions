'''
@author: Santhoshkumar Srinivasan
'''

def histArea(arr):

    #stack = []
    area = []

    for i in range(1, len(arr)):
        rectArea = min(arr[i], arr[i-1])
        for each in area:
            if each <= rectArea:
                area[each] += each
                print("Next", arr[i], area[each], rectArea)
                #prev = area[]
        if rectArea not in area:
            area[rectArea] = rectArea*2
        print("every", rectArea, area)
    print(area)

histArea([6,2,5,1,4,5,1])