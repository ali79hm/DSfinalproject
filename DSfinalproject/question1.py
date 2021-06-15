import os
from stackclass import stack
import copy

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def run():
    myqu1 = q1()
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
            input("press enter to continue...")
            menunumber = "0"
        elif menunumber=="3":
            clearConsole()
            myqu1.printAllPalates()
            input("press enter to continue...")
            menunumber = "0"
        elif menunumber=="exit":
            isloop = False
        else:
            clearConsole()
            menunumber = input("1.add a car \n2.show cars after you\n(for exit type \"exit\")\n")    


class q1:
    def __init__(self):
        self.mystack = stack()
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
        temp = input("please enter a plate number : ")
        if self.serach(self.mystack,temp)==-1:
            self.mystack.push(temp)
            input(f'{self.mystack.peek()} added to stack successfuly. \npress enter to continue...')
        else:
            input(f'cant add plate {temp} to parking list. this plate is already exist!! \npress enter to continue...')
        

    def printplatesafter(self):
        mycarplate = input("please enter your car plate: ")
        mystack = copy.deepcopy(self.mystack)
        ans = self.serach(mystack,mycarplate)
        if ans == -1:
            print("your car isn`t in parking")
        else:
            self.printstack(ans)

    def printstack(self,instack):
        tempstack = copy.deepcopy(instack)
        temp=[]
        if (not tempstack.isEmpty()):
            for i in range(0,tempstack.topIndex+1):
                temp.append(tempstack.pop())
        if temp != None:
            #temp = temp[::-1]
            for plate in temp:
                print(plate)

    def serach(self,mystack,mycarplate):
        index = mystack.topIndex
        tempstack = stack()
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
        mystack = copy.deepcopy(self.mystack)
        index = mystack.topIndex
        tempstack = stack()
        while not mystack.isEmpty():
            temp = mystack.pop()
            tempstack.push(temp)
        self.printstack(tempstack)

    def print(self,type,data): ##nice print
        pass
    




        
