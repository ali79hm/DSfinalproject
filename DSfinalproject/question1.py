import os
from stackclass import stack
from stackclasswithLL import stack as LLstack
import copy

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def printmenu():
    print("select submenu".center(100,"~"))
    print("\n")
    print("1.add a car".center(100," "))
    print("2.show cars after you".center(100," "))
    print("3.show all cars".center(100," "))
    print("(for exit type \"exit\")".center(100," "))
    #"1.add a car \n2.show cars after you\n(for exit type \"exit\")\n"

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
            #print(platenumbers)
            myqu1.printplatesafter()
            menunumber = "0"
        elif menunumber=="3": ## show all plates in parking
            clearConsole()
            myqu1.printAllPalates()
            menunumber = "0"
        elif menunumber=="exit": ##exit
            isloop = False
        else:
            clearConsole()
            printmenu()
            menunumber = input("".center(50," "))
            #menunumber = input("1.add a car \n2.show cars after you\n(for exit type \"exit\")\n")    


class q1:
    def __init__(self,isStackWithLL):
        self.isStackWithLL = isStackWithLL
        if isStackWithLL==False:
            self.mystack = stack()
        else:
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
            #print("!!!error in input data samples!!!")
    
    def addPlate(self):
        print(" add car menu ".center(100,"~"))
        print("\n")
        print("please enter a plate number : ".center(100," "))
        temp = input("".center(47," "))
        if self.serach(self.mystack,temp)==-1:
            self.mystack.push(temp)
            print(f'{self.mystack.peek()} added to parking successfuly.'.center(100," "))
            print("press enter to continue...".center(100," "))
            input("".center(47," "))
        else:
            print(f'cant add plate {temp} to parking list.'.center(100," "))
            print("this plate is already exist!!".center(100," "))
            print("press enter to continue...".center(100," "))
            input("".center(47," "))

    def printplatesafter(self):
        print(" print car menu ".center(100,"~"))
        print("\n")
        print("please enter a plate number : ".center(100," "))
        mycarplate = input("".center(47," "))
        mystack = copy.deepcopy(self.mystack)
        ans = self.serach(mystack,mycarplate)
        if ans == -1:
            print("your car isn`t in parking".center(100," "))
        else:
            self.printstack(ans)
        print("press enter to continue...".center(100," "))
        input("".center(47," "))

    def printstack(self,instack):
        print("".center(100,"\""))
        tempstack = copy.deepcopy(instack)
        temp=[]
        if (not tempstack.isEmpty()):
            for i in range(0,tempstack.topIndex+1):
                temp.append(tempstack.pop())
        if temp != None:
            #temp = temp[::-1]
            for plate in temp:
                print(plate.center(100," "))
        print("".center(100,"\""))

    def serach(self,instack,mycarplate):
        mystack = copy.deepcopy(instack)
        index = mystack.topIndex
        
        if self.isStackWithLL==False:
            tempstack = stack()
        else:
            tempstack = LLstack()
        isfind = False
        while (not mystack.isEmpty()) and (not isfind):
            temp = mystack.pop()
            if temp == mycarplate:
                tempstack.push(temp)
                isfind = True
                return tempstack
                #return None
            else:
                tempstack.push(temp)
        return -1

    def printAllPalates(self):
        print(" print all car menu ".center(100,"~"))
        print("\n")
        mystack = copy.deepcopy(self.mystack)
        index = mystack.topIndex
        if self.isStackWithLL==False:
            tempstack = stack()
        else:
            tempstack = LLstack()
        while not mystack.isEmpty():
            temp = mystack.pop()
            tempstack.push(temp)
        self.printstack(tempstack)
        print("press enter to continue...".center(100," "))
        input("".center(47," "))


    




        
