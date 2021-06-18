from question1 import clearConsole,bcolors
from stackclass import stack
from stackclasswithLL import stack  as LLstack

isStackWithLL= False ## True : Implementation with linked list stack | False : ##Implementation with array stack
def run(isstackWithLL):
    global isStackWithLL 
    isStackWithLL = isstackWithLL
    clearConsole()
    print((bcolors.RED + " algebra equation parantez adder " + bcolors.ENDC).center(110,"~"))
    print("\n")
    print("enter algebra equation:".center(100," "))
    eq = input("".center(40," "))
    eqPasvandi = mianvandiToPasvandi(eq) ## ex: 25*65 => 25 65 *
    eqParantesi = pasvandiToparantes(eqPasvandi) ## ex 25 65 * => (25*65)
    print((bcolors.YELLOW+"↓ parantes form ↓"+ bcolors.ENDC).center(100," "))
    print((bcolors.YELLOW + str(eqParantesi)+ bcolors.ENDC).center(100," "))
    try:
        ans1 = calparantez(eqParantesi) ##calculate answer of parantezi equation
        ans2 = calcPasvandi(eqPasvandi) ##calculate answer of pasvandy equation 
    except:
        ans1 = None
        ans2 = None
    if ans1 != None and ans1==ans2 :
        print("\n")
        print((bcolors.CYAN + f"ans with parantes:{ans1} | ans with olaviat:{ans2} =>" + bcolors.ENDC+bcolors.GREEN + "True" + bcolors.ENDC).center(120," "))
        #print((bcolors.GREEN + "True" + bcolors.ENDC).center(100," "))
    if ans1 == None or ans2 == None:
        print((bcolors.RED + "cant calculate answer to check corrcty of operation but it is True :)" + bcolors.ENDC).center(100," "))

    print("press enter to continue ...".center(100," "))
    input("".center(50," "))

def calcPasvandi(eq): ## calculate answer of pasvandy equation 
    global isStackWithLL
    funcs = [["/","*"],["+","-"]]
    if isStackWithLL==False: ##Implementation with array stack
        mystack = stack()    
    else:                    ## Implementation with linked list stack
        mystack = LLstack()
    neweq = ""
    reset =True ## uses for supporting number with more than 1 digite
    for i,char in enumerate(eq):
        if char == funcs[0][1] or char == funcs[0][0] or char == funcs[1][1] or char == funcs[1][0] : ## if input is " + , - , * , / "
            num2 = float(mystack.pop())
            num1 = float(mystack.pop())
            ans = cal(char,num1,num2)
            mystack.push(str(ans))
        else:
            if reset == True:       ##pushing first digite of number
                mystack.push(char) 
                reset = False
            else:
                if eq[i]==" ":      ## split numbers with space
                    reset = True
                else:               ##pushing other digite of number if exist          
                    temp2 = mystack.pop() 
                    temp2 = temp2 + str(char)
                    mystack.push(temp2)
    while mystack.topIndex>-1:       ##pop answer form stack
        neweq = mystack.pop() + neweq
    return neweq

def calparantez(eq): ##calculate answer of parantezi equation
    while eq.find("(") != -1:
        funcs = [["/","*"],["+","-"]]
        func=0
        befpar = 0
        aftpar = len(eq)-1
        for i in range(len(eq)-1,-1,-1): ##find index of inner "(" and ")"
            if eq[i]=="(":  
                befpar = i
                for j in range(i,len(eq)):
                    if eq[j] == ")":
                        aftpar = j
                        break
                break
        for i in range(befpar+1,aftpar):
            if eq[i] == funcs[0][1] or eq[i] == funcs[0][0] or eq[i] == funcs[1][1] or eq[i] == funcs[1][0] : ## find " + , - , * , / " betwwen paranteses
                char = i
                break
        ans = cal(eq[char],eq[befpar+1:char],eq[char+1:aftpar])
    
        eq = eq[0:befpar]+ str(ans) + eq[aftpar+1:]
    return eq

def cal(func,num1,num2):
    if func=="*":
        ans = float(num1)*float(num2)
    elif func=="/":
        ans = float(num1)/float(num2)
    elif func=="-":
        ans = float(num1)-float(num2)
    else :
        ans = float(num1)+float(num2)
    return ans

def pasvandiToparantes(eq):
    global isStackWithLL
    funcs = [["/","*"],["+","-"]]
    if isStackWithLL==False: ##Implementation with array stack
        mystack = stack()
    else:                   ## Implementation with linked list stack
        mystack = LLstack()
    neweq = ""
    reset =True ## uses for supporting number with more than 1 digite
    for i,char in enumerate(eq):
        if char == funcs[0][1] or char == funcs[0][0] or char == funcs[1][1] or char == funcs[1][0] :
            temp = mystack.pop() + ")"
            temp = char + temp
            temp = "(" + mystack.pop() + temp
            mystack.push(temp)
        else:
            if reset == True:           ##pushing first digite of number
                mystack.push(char)
                reset = False
            else:
                if eq[i]==" ":          ## split numbers with space
                    reset = True
                else:                   ##pushing other digite of number if exist
                    temp2 = mystack.pop()
                    temp2 = temp2 + str(char)
                    mystack.push(temp2)
    while mystack.topIndex>-1:          ##pop answer form stack
        neweq = mystack.pop() + neweq
    return neweq

def mianvandiToPasvandi(eq):
    global isStackWithLL
    funcs = [["/","*"],["+","-"]]
    if isStackWithLL==False:    ##Implementation with array stack
        mystack = stack()
    else:                       ## Implementation with linked list stack
        mystack = LLstack()
    neweq = ""
    for i,char in enumerate(eq):
        if char == funcs[0][1] or char == funcs[0][0]: # '*' , '/'
            beforefunc = mystack.peek()
            if beforefunc == False: ## if stack is empty
                mystack.push(char)
            elif beforefunc == funcs[1][1] or beforefunc == funcs[1][0]: # beforefunc== "-" or "+"
                mystack.push(char)
            else:
                while mystack.topIndex > -1 and (mystack.peek()==funcs[0][1] or mystack.peek()==funcs[0][0]): # beforefunc== "*" or "/"
                    neweq = neweq + str(mystack.pop())
                mystack.push(char)
        elif char == funcs[1][1] or char == funcs[1][0]:# '+' , '-'
             while mystack.topIndex > -1 :##if stack isn`t empty
                 neweq = neweq + str(mystack.pop())
             mystack.push(char)
        else:                                         # numbers
            neweq = neweq + char
            if (i+1<len(eq) and ( eq[i+1]== funcs[0][1] or eq[i+1]== funcs[0][0] or eq[i+1]== funcs[1][1] or eq[i+1]== funcs[1][0])) or i+1==len(eq):
                neweq = neweq + " "
    while(mystack.topIndex!=-1):        
        neweq = neweq + str(mystack.pop())
    return neweq