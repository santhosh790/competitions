''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def palindrome(string):
    if len(string) == 0:
     return 0
    
    count = 0
    vals = [0]*len(string)
    for each in string:
        index = int(each) - 1
        if vals[index] == 1:
            count = count + 1
            vals[index] = 0
        else:
            vals[index] = 1
    return count * 2
def main():

 # Write code here 
 string = input()
 print(palindrome(string), end = '')

main()

