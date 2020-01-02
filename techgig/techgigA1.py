''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def assessIn( villain, hero):
    heroList = hero.strip().split(" ")
    villainList = villain.strip().split(" ") 
    if len(heroList) == len(villainList):
        for each in range(len(heroList)):
            candidate = heroList[each]
            minVal = int(candidate) - int(villainList[0])
            elimVillain = villainList[0]
            for villain in villainList:
                val = int(candidate) - int(villain);
                #print(val)
                if val > 0 and val < minVal:
                    elimVillain = villain
                    minVal = val
            if elimVillain in villainList and minVal > 0:
                villainList.remove(elimVillain)
    
    if len(villainList) == 0:
        return "WIN"
    return "LOSE"
   
def main():

 # Write code here 
 n_itr = input()
 for each in range(int(n_itr)):
     n_in = input()
     print(assessIn(input(),input()))

main()

