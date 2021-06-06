from question1 import run as q1
from question1 import clearConsole


menunumber = "0"
while True:
    if menunumber=="1": ##add palate
        clearConsole()
        q1()
        menunumber = "0"
    else:
        clearConsole()
        menunumber = input("1.question one \n2.question two\n")