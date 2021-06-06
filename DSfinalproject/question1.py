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
        if menunumber=="1": ##add palate
            clearConsole()
            temp = input("please enter a plate number : ")
            myqu1.mystack.push(temp)
    
            input(f'{myqu1.mystack.peek()} added to stack successfuly. press enter to continue...')
            menunumber = "0"
        elif menunumber=="2": ##show back palates
            clearConsole()
            #print(platenumbers)
            temp = input("please enter your car plate: ")
            myqu1.printPalates(myqu1.mystack,temp)
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
            datafile = open("data.txt", "r")
            platenumbers = datafile.read().splitlines()
            for plate in platenumbers:
                self.mystack.push(plate)
            datafile.close()
            del platenumbers
        except:
            pass
            #print("!!!error in input data samples!!!")
    

    def printstack(self,tempstack):
        temp=[]
        if (not tempstack.isEmpty()):
            for i in range(0,tempstack.topIndex+1):
                temp.append(tempstack.pop())
        if temp != None:
            #temp = temp[::-1]
            for plate in temp:
                print(plate)

    def printPalates(self,instack,mycarplate):
        mystack = copy.deepcopy(instack)
        index = mystack.topIndex
        tempstack = stack()
        isfind = False
        while (not mystack.isEmpty()) and (not isfind):
            temp = mystack.pop()
            if temp == mycarplate:
                tempstack.push(temp)
                self.printstack(tempstack)
                isfind = True
                #return None
            else:
                tempstack.push(temp)
    




        
