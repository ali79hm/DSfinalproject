from question1 import run as q1
from question2 import run as q2
from question3 import run as q3
from question4 import run as q4
from question1 import clearConsole,bcolors


  
def printmenu():
    print((bcolors.RED + "select project part" + bcolors.ENDC).center(110,"~"))
    print("\n")
    print("1.question one (president party)".center(100," "))
    print("2.question two (algebra equations)".center(100," "))
    print("3.question three (colored circles)".center(100," "))
    print("4.question four (jolipotous prison)".center(100," "))


isStackWithLL = False
isQueueWithLL = False 

print("DSproject".center(100,"~"))
print("seyed ali hosseini".center(100," "))
print("\n")
print("select your setting :".center(100," "))
print("00- stack with array | queue with array".center(100," "))
print("01- stack with array | queue with linkedlist".center(100," "))
print("10- stack with linkedlist | queue with array".center(100," "))
print("11- stack with linkedlist | queue with linkedlist".center(100," "))
set = input("".center(50," "))

if len(set)>0 and set[0]=="1":
    isStackWithLL = True
if len(set)>1 and set[1]=="1":
    isQueueWithLL = True

menunumber = "0"
while True:
    if menunumber=="1":
        clearConsole()
        q1(isStackWithLL)
        menunumber = "0"
    elif menunumber=="2": 
        clearConsole()
        q2(isStackWithLL)
        menunumber = "0"
    elif menunumber == "3":
        clearConsole()
        q3(isStackWithLL)
        menunumber = "0"
    elif menunumber =="4":
        clearConsole()
        q4(isQueueWithLL)
        menunumber = "0"
    else:
        clearConsole()
        printmenu()
        menunumber = input("".center(50," "))
 
