import os
from stackclass import stack
from stackclasswithLL import stack as LLstack
import copy

class bcolors: ##color fo console
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def printmenu():
    print((bcolors.RED + " president party " + bcolors.ENDC).center(110,"~"))
    print("\n")
    print("1.add a car".center(100," "))
    print("2.show cars after you".center(100," "))
    print("3.show all cars".center(100," "))
    print("(for exit type \"exit\")".center(100," "))

def run(isStackWithLL):
    myqu1 = q1(isStackWithLL)
    menunumber="0"
    isloop =  True
    while isloop:
        if menunumber=="1": ##add plate
            clearConsole()
            myqu1.addPlate()
            menunumber = "0"
        elif menunumber=="2": ##show palates after you
            clearConsole()
            myqu1.printplatesafter()
            menunumber = "0"
        elif menunumber=="3": ## show all plates in parking
            clearConsole()
            myqu1.printAllPalates()
            menunumber = "0"
        elif menunumber=="exit": ##exit
            isloop = False
        else:
            clearConsole()  ##print menu
            printmenu()
            menunumber = input("".center(50," "))

class q1:
    def __init__(self,isStackWithLL):
        self.isStackWithLL = isStackWithLL
        if isStackWithLL==False:    ## Implementation with array stack
            self.mystack = stack()
        else:                       ## Implementation with linked list stack
            self.mystack = LLstack()
        try:
            datafile = open("data.txt", "r") ##import some plates
            platenumbers = datafile.read().splitlines()
            for plate in platenumbers:
                self.mystack.push(plate)
            datafile.close()
            del platenumbers
        except:
            pass
    
    def addPlate(self): ## add plate tp stack
        print((bcolors.RED + " add car menu " + bcolors.ENDC).center(110,"~"))
        print("\n")
        print("please enter a plate number : ".center(100," "))
        temp = input("".center(47," "))
        if self.serach(self.mystack,temp)==-1:
            self.mystack.push(temp)
            print((bcolors.GREEN + f'{self.mystack.peek()} added to parking successfuly.' + bcolors.ENDC).center(110," "))
            print("press enter to continue...".center(100," "))
            input("".center(47," "))
        else:
            print((bcolors.RED + f'cant add plate {temp} to parking list.' + bcolors.ENDC).center(110," "))
            print((bcolors.RED + "this plate is already exist!!" + bcolors.ENDC).center(110," "))
            print("press enter to continue...".center(100," "))
            input("".center(47," "))

    def printplatesafter(self): ##print plates after enterd plate 
        print((bcolors.RED + " print car menu " + bcolors.ENDC).center(110,"~"))
        print("\n")
        print("please enter a plate number : ".center(100," "))
        mycarplate = input("".center(47," "))
        mystack = copy.deepcopy(self.mystack)
        ans = self.serach(mystack,mycarplate)
        if ans == -1:
            print((bcolors.RED + "your car isn`t in parking" + bcolors.ENDC).center(110," "))
        else:
            self.printstack(ans)
        print("press enter to continue...".center(100," "))
        input("".center(47," "))

    def printstack(self,instack): 
        print(((bcolors.BLUE +"~" + bcolors.ENDC)*100))
        tempstack = copy.deepcopy(instack)
        temp=[]
        if (not tempstack.isEmpty()):
            for i in range(0,tempstack.topIndex+1):
                temp.append(tempstack.pop())
        if temp != None:
            for plate in temp:
                print(plate.center(100," "))
        print(((bcolors.BLUE +"~" + bcolors.ENDC)*100))

    def serach(self,instack,mycarplate): ##serach in stack 
        mystack = copy.deepcopy(instack)
        index = mystack.topIndex
        
        if self.isStackWithLL==False:   ## Implementation with array stack
            tempstack = stack()
        else:                           ## Implementation with linked list stack
            tempstack = LLstack()
        isfind = False
        while (not mystack.isEmpty()) and (not isfind):
            temp = mystack.pop()
            if temp == mycarplate:
                tempstack.push(temp)
                isfind = True
                return tempstack
            else:
                tempstack.push(temp)
        return -1

    def printAllPalates(self): ##print all plates
        print((bcolors.RED + " print all car menu " + bcolors.ENDC).center(110,"~"))
        print("\n")
        mystack = copy.deepcopy(self.mystack)
        index = mystack.topIndex
        if self.isStackWithLL==False:   ## Implementation with array stack
            tempstack = stack()
        else:                           ## Implementation with linked list stack
            tempstack = LLstack()
        while not mystack.isEmpty():
            temp = mystack.pop()
            tempstack.push(temp)
        self.printstack(tempstack)
        print("press enter to continue...".center(100," "))
        input("".center(47," "))


    




        
