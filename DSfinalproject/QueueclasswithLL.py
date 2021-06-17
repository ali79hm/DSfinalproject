from linkedlistclass import LinkedList

class Queue:
    
    def __init__(self,size):
        self.Queuedata = LinkedList()
        #self.Queuedata = []
        self.front = 0
        self.rear = 0
        self.max = size

    def getQueuedata(self):
        return self.Queuedata.getList()
        #return self.Queuedata

    def getCount(self):
        return len(self.Queuedata.getList())
        #return len(self.Queuedata)

    def Enqueue(self,data):
        if self.rear != self.max:
            self.rear = self.rear+1
            self.Queuedata.InsertNode(data)
            #self.Queuedata.append(data)
            return True
        else:
            #print("Queue Overflow")
            return False
    def Dequeue(self):
        if self.rear != self.front:
            self.rear = self.rear-1
            temp = self.Queuedata.getNode(0)
            temp = temp.data
            self.Queuedata.DeleteNodewithindex(0)
            return temp
            #return self.Queuedata.pop(0)
        else:
            #print("Queue is Empty")
            return -1
            

