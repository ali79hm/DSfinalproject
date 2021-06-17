class Queue:
    
    def __init__(self,size):
        self.Queuedata = []
        self.front = 0
        self.rear = 0
        self.max = size

    def getQueuedata(self):
        return self.Queuedata

    def getCount(self):
        return len(self.Queuedata)

    def Enqueue(self,data):
        if self.rear != self.max:
            self.rear = self.rear+1
            self.Queuedata.append(data)
        else:
            #print("Queue Overflow")
            print()

    def Dequeue(self):
        if self.rear != self.front:
            self.rear = self.rear-1
            return self.Queuedata.pop(0)
        else:
            #print("Queue is Empty")
            return -1
            
