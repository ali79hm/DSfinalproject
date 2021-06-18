from random import randint,choice
from stackclass import stack
from question1 import clearConsole,bcolors
from stackclasswithLL import stack  as LLstack


line1 = None
line2 = None
line3 = None

def run(isStackWithLL):
    global line1,line2,line3
    if isStackWithLL==False: ##Implementation with linked list stack
        line1 = stack()
        line2 = stack()
        line3 = stack()
    else:                   ##Implementation with array stack
        line1 = LLstack()
        line2 = LLstack()
        line3 = LLstack()
    initializelines()
    while(not checkwin()): ##loop untin win
        print((bcolors.RED + " color rings game " + bcolors.ENDC).center(110,"~"))
        #print(" color rings game ".center(100,"~"))
        print("\n")
        print("for moving numbers use this commend:".center(100," "))
        print("A B".center(100," "))
        print("this will move line A to line B".center(100," "))
        print((bcolors.UNDERLINE + "(for exit type exit)" + bcolors.ENDC).center(105," "))
        printlines()
    
        cmd = input(">> ") ## game controller input
        if(cmd == "exit"):
            return 0
        cmd = cmd.split()
        if len(cmd)== 2:
            manage(cmd)
        clearConsole()

    printlines() 
    print("\n")
    print("".center(100,"~"))
    print("       ".center(100,"~"))
    print((bcolors.RED + " you win " + bcolors.ENDC).center(110,"~"))
    print("       ".center(100,"~"))
    print("".center(100,"~"))
    print("press enter to continue ...".center(100," "))
    input("".center(50," "))

def checkwin(): ##check if playes won or not (return True if player wins)
    global line1,line2,line3
    flag1 = 0 #show if line1 is sorted
    flag2 = 0 #show if line2 is sorted
    flag3 = 0 #show if line3 is sorted
    data1 = line1.getstackdata() 
    data2 = line2.getstackdata()
    data3 = line3.getstackdata()
    if(data1 == sorted(data1) or data1 == sorted(data1,reverse = True)): #check if line1 is sorted
        flag1 = 1
    if(data2 == sorted(data2) or data2 == sorted(data2,reverse = True)): #check if line2 is sorted
        flag2 = 1
    if(data3 == sorted(data3) or data3 == sorted(data3,reverse = True)): #check if line3 is sorted
        flag3 = 1
    if(flag1 and flag2 and flag3): # if all lines sorted return True
        return True
    return False

def initializelines(): ##divide 1 to 15 in 3 line randomly
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    global line1,line2,line3
    l1Size = randint(0,15)
    l2Size = randint(0,15-l1Size)
    l3Size = 15 - l2Size - l1Size

    for i in range(0,l1Size):
        temp = choice(numbers)
        numbers.remove(temp)
        line1.push(temp)
    for i in range(0,l2Size):
        temp = choice(numbers)
        numbers.remove(temp)
        line2.push(temp)
    for x in numbers:
        line3.push(x)

def printlines(): ##print lines data
    spaces = 100 # for centerize texts
    global line1,line2,line3
    data1 = line1.getstackdata()
    data2 = line2.getstackdata()
    data3 = line3.getstackdata()
    print((bcolors.RED + "#" + bcolors.ENDC)*100)
    maxsize =max([line1.topIndex,line2.topIndex,line3.topIndex])
    for i in range(maxsize,-1,-1):
        mystr = ""
        try:
            mystr = mystr + str(data1[i])
            if(data1[i]<10):
                mystr = mystr + "   "
            else:
                mystr = mystr + "  "
        except:
            mystr = mystr + "    "
        try:
            mystr = mystr + str(data2[i])
            if(data2[i]<10):
                mystr = mystr + "   "
            else:
                mystr = mystr + "  "
        except:
            mystr = mystr + "    "

        try:
            mystr = mystr + str(data3[i])
            if(data3[i]<10):
                mystr = mystr + " "
        except:
            mystr = mystr + "  "
        print(mystr.center(spaces))
    print((bcolors.BLUE + "||  ||  ||"+ bcolors.ENDC).center(spaces+10))
    print("01  02  03".center(spaces))
    print((bcolors.RED + "#" + bcolors.ENDC)*100)

def manage(cmd): ##manage input commends like: "A B"
    global line1,line2,line3
    temp = ""
    if  not(int(cmd[1])>3 or  int(cmd[1])<1):
        if int(cmd[0])==1:
            temp = line1.pop()
        elif int(cmd[0])==2:
            temp = line2.pop()
        elif int(cmd[0])==3:
            temp = line3.pop()

       
    if temp !="" and (int(temp)<16 and int(temp)>0):
        if int(cmd[1])==1:
            line1.push(temp)
        elif int(cmd[1])==2:
            line2.push(temp)
        elif int(cmd[1])==3:
            line3.push(temp)



