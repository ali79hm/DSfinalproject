from question1 import run as q1
from question2 import run as q2
from question3 import run as q3
from question4 import run as q4
from question1 import clearConsole
#from linkedlistclass import *

def printmenu():
    print("select project part".center(100,"~"))
    print("\n")
    print("1.question one".center(100," "))
    print("2.question two".center(100," "))
    print("3.question three".center(100," "))
    print("4.question four".center(100," "))


#ml = LinkedList()
#ml.InsertNode("four",0)
#ml.InsertNode("three",0)
#ml.InsertNode("two",0)
#ml.InsertNode("one",0)
#ml.InsertNode("ziro",0)
##ml.InsertNode("shod be in index last")
#ml.DisplayList()
#ml.DeleteNodewithindex(2)
#print("\n")
#ml.DisplayList()

isStackWithLL = False
isQueueWithLL = False 

#input("press any kay to continue ...")
print("DSproject".center(100,"~"))
print("seyed ali hosseini".center(100," "))
print("\n")
print("select your setting :".center(100," "))
print("00- stack with array | queue with array".center(100," "))
print("01- stack with array | queue with linkedlist".center(100," "))
print("10- stack with linkedlist | queue with array".center(100," "))
print("11- stack with linkedlist | queue with linkedlist".center(100," "))
set = input("".center(50," "))

if set[0]=="1":
    isStackWithLL = True
if set[1]=="1":
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
        q4()
        menunumber = "0"
    else:
        clearConsole()
        #print("1.question one \n2.question two\n2.question three\n")
        printmenu()
        menunumber = input("".center(50," "))
 
