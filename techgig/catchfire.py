''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT




def getCountOfFieldFire(dimension, rows, fireAt0):
    
    if len(fireAt0) == 0:
        return -1
    
    xCoordinate = int(dimension[0])
    yCoordinate = int(dimension[1])
    
    
    iterations = 0
    
    totalFields = xCoordinate * yCoordinate
    totalFields = totalFields - len(fireAt0)
    while totalFields > 0:
        iterations = iterations + 1
        #print("iterations"+str(iterations))
        newFireC = []
        for each in fireAt0:
            x = each[0]
            y = each[1]
            if x>= xCoordinate and y >= yCoordinate:
                return
            else:
                #print("coordinates-{} -- {}".format(x,y))
                if x-1 >=0 and rows[x-1][y] != '1':
                    rows[x-1][y] = '1'
                    totalFields = totalFields - 1
                    newFireC.append([x-1,y])
                if y-1 >=0 and rows[x][y-1] != '1':
                    rows[x][y-1] = '1'
                    totalFields = totalFields - 1
                    newFireC.append([x,y-1])
                if x+1 < xCoordinate and rows[x+1][y] != '1':
                    rows[x+1][y] = '1'
                    totalFields = totalFields - 1
                    newFireC.append([x+1,y])
                if y+1 < yCoordinate and rows[x][y+1] != '1':
                    rows[x][y+1] = '1'
                    totalFields = totalFields - 1
                    newFireC.append([x,y+1])
                #print(newFireC)
                #print(totalFields)
                #print("itermations:"+str(iterations))
        fireAt0 = newFireC 
        
    return iterations


def main():

 # Write code here 
 dimension = input().split()
 rows = []
 #print(dimension)
 #print(input())
 fireAt0 = []
 for i in range(int(dimension[0])):
     fieldRow = input()
     if fieldRow.find('1') != -1:
         for index, each in enumerate(fieldRow.split()):
             if each == '1':
                 fireAt0.append([i,index])
                 #print(index)
                 #print("vale"+each)
     rows.append(fieldRow.split())

 print(getCountOfFieldFire(dimension, rows,fireAt0),end='')

main()

