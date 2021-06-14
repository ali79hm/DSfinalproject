from question1 import run as q1
from question2 import run as q2
from question3 import run as q3
from question4 import run as q4
from question1 import clearConsole
from linkedlistclass import *



#ml = LinkedList()
#ml.InsertNode("one")
#ml.InsertNode("two")
#ml.InsertNode("three")
#ml.InsertNode("four")
#ml.InsertNode("five")
#ml.InsertNode("shod be in index last",-1)
#ml.DisplayList()
#ml.DeleteNode("three")
#print("\n")
#ml.DisplayList()


#input("press any kay to continue ...")

#q4()
menunumber = "0"
while True:
    if menunumber=="1":
        clearConsole()
        q1()
        menunumber = "0"
    elif menunumber=="2": 
        clearConsole()
        q2()
        menunumber = "0"
    elif menunumber == "3":
        clearConsole()
        q3()
        menunumber = "0"
    elif menunumber =="4":
        clearConsole()
        q4()
        menunumber = "0"
    else:
        clearConsole()
        print("1.question one \n2.question two\n2.question three\n")
        menunumber = input(">> ")
        