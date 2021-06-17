from question1 import clearConsole
from stackclass import stack
from stackclasswithLL import stack  as LLstack

isStackWithLL= False
def run(isstackWithLL):
    global isStackWithLL
    isStackWithLL = isstackWithLL
    clearConsole()
    #temp = input("enter your algebraic expression")
    #findallChars()
    print("select project part".center(100,"~"))
    print("\n")
    print("enter algebra equation:".center(100," "))
    eq = input("".center(40," "))
    #eq = input(">> ")
    #eq = "2+3*4*5+2"
    #eq = "2*5+4*5+6+8*5" ##del
    #eq="2+2*3"
    #print(eq)
    eqPasvandi = mianvandiToPasvandi(eq)
    eqParantesi = pasvandiToparantes(eqPasvandi)
    print("↓ parantez form ↓".center(100," "))
    print(str(eqParantesi).center(100," "))
    #parantesToPasvandi(eqParantesi)
    try:
        ans1 = calparantez(eqParantesi)
        ans2 = calcPasvandi(eqPasvandi)
    except:
        ans1 = None
        ans2 = None
    if ans1==ans2 : 
        print("True".center(100," "))
    if ans1 == None or ans2 == None:
        print("cant calculate answer to check corrcty of operation".center(100," "))

    #print(mianvandiToPasvandi(eq))
    #print(pasvandiToparantes(mianvandiToPasvandi(eq)))
    #addpr("","")
    print("press enter to continue ...".center(100," "))
    input("".center(50," "))


def calcPasvandi(eq):
    global isStackWithLL
    funcs = [["/","*"],["+","-"]]
    if isStackWithLL==False:
        mystack = stack()
    else:
        mystack = LLstack()
    neweq = ""
    reset =True
    for i,char in enumerate(eq):
        if char == funcs[0][1] or char == funcs[0][0] or char == funcs[1][1] or char == funcs[1][0] :
            num2 = float(mystack.pop())
            num1 = float(mystack.pop())
            ans = cal(char,num1,num2)
            mystack.push(str(ans))
        else:
            if reset == True:
                mystack.push(char)
                reset = False
            else:
                if eq[i]==" ":
                    reset = True
                else:
                    temp2 = mystack.pop()
                    temp2 = temp2 + str(char)
                    mystack.push(temp2)
    while mystack.topIndex>-1:
        neweq = mystack.pop() + neweq
    return neweq
def calparantez(eq):
    #eq = "((((6/3)+12)-((16/12)*9))+25)"
    while eq.find("(") != -1:
        funcs = [["/","*"],["+","-"]]
        func=0
        befpar = 0
        aftpar = len(eq)-1
        for i in range(len(eq)-1,-1,-1):
            if eq[i]=="(":
                befpar = i
                for j in range(i,len(eq)):
                    if eq[j] == ")":
                        aftpar = j
                        break
                break
        for i in range(befpar+1,aftpar):
            if eq[i] == funcs[0][1] or eq[i] == funcs[0][0] or eq[i] == funcs[1][1] or eq[i] == funcs[1][0] :
                char = i
                break
        ans = cal(eq[char],eq[befpar+1:char],eq[char+1:aftpar])
    
        eq = eq[0:befpar]+ str(ans) + eq[aftpar+1:]
    return eq
            #myeq = char+eq[befpar+1:i]+" "+eq[i+1:aftpar]+" "
           
            #eq = eq[0:befpar]+myeq + eq[aftpar+1:]
            #print()

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
    if isStackWithLL==False:
        mystack = stack()
    else:
        mystack = LLstack()
    neweq = ""
    reset =True
    for i,char in enumerate(eq):
        if char == funcs[0][1] or char == funcs[0][0] or char == funcs[1][1] or char == funcs[1][0] :
            temp = mystack.pop() + ")"
            temp = char + temp
            temp = "(" + mystack.pop() + temp
            mystack.push(temp)
        else:
            if reset == True:
                mystack.push(char)
                reset = False
            else:
                if eq[i]==" ":
                    reset = True
                else:
                    temp2 = mystack.pop()
                    temp2 = temp2 + str(char)
                    mystack.push(temp2)
                

            

    while mystack.topIndex>-1:
        neweq = mystack.pop() + neweq
    return neweq
def mianvandiToPasvandi(eq):
    global isStackWithLL
    funcs = [["/","*"],["+","-"]]
    #eq = "2*5+4*5+6+8*5" ###del
    if isStackWithLL==False:
        mystack = stack()
    else:
        mystack = LLstack()
    neweq = ""
    for i,char in enumerate(eq):
        if char == funcs[0][1] or char == funcs[0][0]: # '*' , '/'
            beforefunc = mystack.peek()
            if beforefunc == False:
                mystack.push(char)
            elif beforefunc == funcs[1][1] or beforefunc == funcs[1][0]:
                mystack.push(char)
            else:
                while mystack.topIndex > -1 and (mystack.peek()==funcs[0][1] or mystack.peek()==funcs[0][0]):
                    neweq = neweq + str(mystack.pop())
                mystack.push(char)
        elif char == funcs[1][1] or char == funcs[1][0]:
             while mystack.topIndex > -1 :
                 neweq = neweq + str(mystack.pop())
             mystack.push(char)
        else:
            neweq = neweq + char
            if (i+1<len(eq) and ( eq[i+1]== funcs[0][1] or eq[i+1]== funcs[0][0] or eq[i+1]== funcs[1][1] or eq[i+1]== funcs[1][0])) or i+1==len(eq):
                neweq = neweq + " "
    while(mystack.topIndex!=-1):
        neweq = neweq + str(mystack.pop())
    return neweq