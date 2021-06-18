from Queueclass import Queue
from QueueclasswithLL import Queue as LLQueue
from question1 import clearConsole,bcolors
import time
import threading


def run(isQueueWithLL):
    newjail = jail(isQueueWithLL) ##creat jail object
    threadnNames = [newjail.printlocation,newjail.mngPower,newjail.MngCorridor,newjail.Mngstairs,newjail.MngResturant,newjail.Mngyard]
    threads = []
    for x in threadnNames: ## add functions to separate threads
        t = threading.Thread(target=x)
        threads.append(t)
        t.start()
    input("") ## wait for enter to exit
    newjail.stop()

class jail:
    def __init__(self,isQueueWithLL):
        js = ["j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10", "j11", "j12", "j13", "j14", "j15", "j16", "j17", "j18", "j19", "j20", "j21", "j22", "j23", "j24", "j25", "j26", "j27", "j28", "j29", "j30", "j31", "j32", "j33", "j34", "j35", "j36", "j37", "j38", "j39", "j40"]
        if isQueueWithLL==True: ##Implementation with linked list queue
            self.resturant = LLQueue(1)
            self.stairs = LLQueue(8)
            self.Corridor = LLQueue(40)
            self.yard = LLQueue(40)
        else:                   ##Implementation with array queue
            self.resturant = Queue(1)
            self.stairs = Queue(8)
            self.Corridor = Queue(40)
            self.yard = Queue(40)
        self.ThreadRun = True ##if == False => all threads will stop
        self.startTime = -5
        for j in js: ## add jolipotoses to queue
            self.Corridor.Enqueue(j) 

    def stop(self): ##stop cycle
        self.ThreadRun = False

    def MngResturant(self): ##manage people in resturnat queue (every 5s ,one person will go out of queue)
        while(self.ThreadRun):
            if self.resturant.getCount()>0:
                time.sleep(5)
                temp = self.resturant.Dequeue()
                self.yard.Enqueue(temp)

    def Mngstairs(self): ##manage people in stairs queue (every time resturant is empty ,one person will go out of queue)
        while(self.ThreadRun):
            if self.stairs.getCount()>0 and self.resturant.getCount()<1:
                temp = self.stairs.Dequeue()
                self.resturant.Enqueue(temp)


    def MngCorridor(self): ##manage people in Corridor queue (every time stairs has empty cell ,one person will go out of queue)
        while(self.ThreadRun):
            if self.Corridor.getCount()>0 and self.stairs.getCount()<8:
                temp = self.Corridor.Dequeue()
                self.stairs.Enqueue(temp)
                

    def mngPower(self): ##manage Electricity (every 50s powerfails and all people in stairs will go to end of Corridor queue)
        while(self.ThreadRun):
            time.sleep(50)
            if self.ThreadRun:
                print("powerfail")
                for i in range(0,self.stairs.getCount()):
                    tmp = self.stairs.Dequeue()
                    print(str(tmp)+" back to Corridor")
                    self.Corridor.Enqueue(tmp)


    def Mngyard(self): ##manage people in yard queue (every 120s ,one person will go out of queue)
        while(self.ThreadRun):
            if self.yard.getCount()>0:
                time.sleep(120)
                temp = self.yard.Dequeue()
                self.Corridor.Enqueue(temp)

    def printlocation(self): # show Condition of all people in jail , colorful! :)
        while(self.ThreadRun):
            clearConsole()
            self.startTime = self.startTime+5
            print((bcolors.RED + " jolipotos jail " + bcolors.ENDC).center(110,"~"))
            print((bcolors.UNDERLINE + "(for exit press enter)" + bcolors.ENDC).center(110," "))
            print('\n')
            print(bcolors.YELLOW + str(self.startTime)+" second is passed" + bcolors.ENDC)
            print(bcolors.GREEN + "\n================================================================================" + bcolors.ENDC)
            print("Corridor: "+str(self.Corridor.getQueuedata()))
            print(bcolors.BLUE+"------------------------------------------------------------------------------" + bcolors.ENDC)
            print("stairs: "+str(self.stairs.getQueuedata()))
            print(bcolors.BLUE+"------------------------------------------------------------------------------" + bcolors.ENDC)
            print("resturant: "+str(self.resturant.getQueuedata()))
            print(bcolors.BLUE +"------------------------------------------------------------------------------" + bcolors.ENDC)
            print("yard: "+str(self.yard.getQueuedata()))
            print(bcolors.GREEN +"\n================================================================================" + bcolors.ENDC)
            time.sleep(5)
            
