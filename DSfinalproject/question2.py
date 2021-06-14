from question1 import clearConsole

def run():
    clearConsole()
    #temp = input("enter your algebraic expression")
    #findallChars()
    print("enter algebra equation: ")
    #eq = input(">> ")
    #eq = "2+3*4*5+2"
    eq = "2*5+4*5+6+8*5"
    manageOlaviat(eq)
    #addpr("","")
    input("press enter to continue ...")

def manageOlaviat(eq):
    eq = addpr(eq,"*")
    eq = addpr(eq,"+")
def addpr(eq,char):
    loop = True
    while(loop):
        i=-1
        while(i<len(eq)):
            i = i+1
            if eq[i] == "(":
                for j in range(len(eq)-1,i,-1):
                    if(eq[j] == ")"):
                        i=j
                        break
            if(eq[i]==char):
                bfIndex = i
                afIndex = i
                j=i
                while(j<len(eq)):
                    j = j+1
                    if eq[j] == "(":
                        for h in range(len(eq)-1,j,-1):
                            if eq[h] == ")":
                                j = h
                                break
                    if j+1 >= len(eq): ##
                        afIndex = len(eq) ##
                        break ##
                    if eq[j] == "+" or eq[j] == "-" or eq[j] == "/" or eq[j] == "*":
                        afIndex = j
                        break
                j=i
                while j>0:
                    j= j-1
                    if eq[j] == ")":
                        for h in range(0,j):
                            if eq[h] == "(":
                                j = h
                                break
                    if j-1 < 0: ##
                        bfIndex = -1##
                        break ##
                    if eq[j] == "+" or eq[j] == "-" or eq[j] == "/" or eq[j] == "*":
                        bfIndex = j
                        break

                
                eq = eq[0:bfIndex+1] + "(" + eq[bfIndex+1:afIndex]+")"+eq[afIndex:len(eq)]
                break
            elif(i == len(eq)-1):
                loop = False
                break
        print(eq)
    return eq

