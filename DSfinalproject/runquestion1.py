from stackclass import stack
from DSfinalproject import clearConsole
import copy

def run():
    myqu1 = q1()
    menunumber="0"
    while True:
        if menunumber=="1": ##add palate
            clearConsole()
            temp = input("please enter a plate number : ")
            myqu1.mystack.push(temp)
    
            input(f'{mystack.peek()} added to stack successfuly. press enter to continue...')
            menunumber = "0"
        elif menunumber=="2": ##show back palates
            clearConsole()
            #print(platenumbers)
            temp = input("please enter your car plate: ")
            myqu1.printPalates(myqu1.mystack,temp)
            input("press enter to continue...")
            menunumber = "0"

        else:
            clearConsole()
            menunumber = input("1.add a car \n2.show cars after you\n")   