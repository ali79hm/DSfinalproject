from Queueclass import Queue
import time
#import _thread as thread
import threading
from question1 import clearConsole


def run():
    #print("ali")
    newjail = jail()
    threadnNames = [newjail.printlocation,newjail.mngPower,newjail.MngCorridor,newjail.Mngstairs,newjail.MngResturant,newjail.Mngyard]
    threads = []
    for x in threadnNames:
        t = threading.Thread(target=x)
        threads.append(t)
        t.start()
    
    #t = threading.Thread(target=threadnNames[0])
    #thread.start_new_thread( newjail.printlocation)
    #threads.append(t)
    #t.start()

    
    #thread.start_new_thread( newjail.mngPower)
    ###print(str(newjail.Corridor.getQueuedata()))
    #thread.start_new_thread( newjail.MngCorridor)
    #thread.start_new_thread( newjail.Mngstairs)
    #thread.start_new_thread( newjail.MngResturant)
    #thread.start_new_thread( newjail.Mngyard)
    
    


    input("")
    newjail.stop()
    #return 0

class jail:
    def __init__(self):
        js = ["j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10", "j11", "j12", "j13", "j14", "j15", "j16", "j17", "j18", "j19", "j20", "j21", "j22", "j23", "j24", "j25", "j26", "j27", "j28", "j29", "j30", "j31", "j32", "j33", "j34", "j35", "j36", "j37", "j38", "j39", "j40"]
        self.resturant = Queue(1)
        self.stairs = Queue(8)
        self.Corridor = Queue(40)
        self.yard = Queue(40)
        self.ThreadRun = True
        self.startTime = -5
        #self.noPowerFlag = threading.Event()
        for j in js:
            self.Corridor.Enqueue(j)

    def stop(self):
        self.ThreadRun = False
    def MngResturant(self):
        while(self.ThreadRun):
            if self.resturant.getCount()>0:
                time.sleep(5)
                temp = self.resturant.Dequeue()
                self.yard.Enqueue(temp)

    def Mngstairs(self):
        while(self.ThreadRun):
            if self.stairs.getCount()>0 and self.resturant.getCount()<1:
                temp = self.stairs.Dequeue()
                self.resturant.Enqueue(temp)


    def MngCorridor(self):
        while(self.ThreadRun):
            #if self.noPowerFlag.is_set():
            #    self.noPowerFlag.clear()
            #    time.sleep(4)
            if self.Corridor.getCount()>0 and self.stairs.getCount()<8:
                temp = self.Corridor.Dequeue()
                self.stairs.Enqueue(temp)
                

    def mngPower(self):
        while(self.ThreadRun):
            time.sleep(50)
            print("powerfail")
            #self.noPowerFlag.set()
            for i in range(0,self.stairs.getCount()):
                tmp = self.stairs.Dequeue()
                print(str(tmp)+" back to Corridor")
                self.Corridor.Enqueue(tmp)


    def Mngyard(self):
        while(self.ThreadRun):
            if self.yard.getCount()>0:
                time.sleep(120)
                temp = self.yard.Dequeue()
                self.Corridor.Enqueue(temp)

    def printlocation(self):
        while(self.ThreadRun):
            clearConsole()
            self.startTime = self.startTime+5
            print(str(self.startTime)+" second is passed")
            print("\n================================================================================")
            print("Corridor: "+str(self.Corridor.getQueuedata()))
            print("------------------------------------------------------------------------------")
            print("stairs: "+str(self.stairs.getQueuedata()))
            print("------------------------------------------------------------------------------")
            print("resturant: "+str(self.resturant.getQueuedata()))
            print("------------------------------------------------------------------------------")
            print("yard: "+str(self.yard.getQueuedata()))
            print("================================================================================")
            time.sleep(5)
            
