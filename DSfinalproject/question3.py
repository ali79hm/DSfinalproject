from random import randint,choice
from stackclass import stack
from question1 import clearConsole
from stackclasswithLL import stack  as LLstack


line1 = None
line2 = None
line3 = None

def run(isStackWithLL):
    global line1,line2,line3
    if isStackWithLL==False:
        line1 = stack()
        line2 = stack()
        line3 = stack()
    else:
        line1 = LLstack()
        line2 = LLstack()
        line3 = LLstack()
    initializelines()
    while(not checkwin()):
        print(" color rings game ".center(100,"~"))
        print("\n")
        print("for moving numbers use this commend:".center(100," "))
        print("A B".center(100," "))
        print("this will move line A to line B".center(100," "))
        print("(for exit type \"exit\")".center(100," "))
        #print("\n \n\n")
        printlines()
    
        cmd = input(">> ")
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
    print(" you win ".center(100,"~"))
    print("       ".center(100,"~"))
    print("".center(100,"~"))
    print("press enter to continue ...".center(100," "))
    input("".center(50," "))
    
    


def checkwin():
    global line1,line2,line3
    flag1 = 0
    flag2 = 0
    flag3 = 0
    data1 = line1.getstackdata()
    data2 = line2.getstackdata()
    data3 = line3.getstackdata()
    if(data1 == sorted(data1) or data1 == sorted(data1,reverse = True)):
        flag1 = 1
    if(data2 == sorted(data2) or data2 == sorted(data2,reverse = True)):
        flag2 = 1
    if(data3 == sorted(data3) or data3 == sorted(data3,reverse = True)):
        flag3 = 1
    if(flag1 and flag2 and flag3):
        return True
    return False
def initializelines():
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
def printlines():
    spaces = 100
    global line1,line2,line3
    data1 = line1.getstackdata()
    data2 = line2.getstackdata()
    data3 = line3.getstackdata()
    print("".center(spaces,"#"))
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
    print("||  ||  ||".center(spaces))
    print("01  02  03".center(spaces))
    print("".center(spaces,"#"))
def manage(cmd):
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



