
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def teamed(count):
    if count == 2:
        return 1
    elif count == 3:
        return 2
    return count // 2 + teamed(count//2 + count % 2)

def findTeams(teams):
    for each in teams:
        fin = int(each) - 1
        print(teamed(int(each)))


def main():

 # Write code here 
 nos = int(input())
 
 teams = []

 for each in range(nos):
     teams.append(input())

 findTeams(teams)

main()

