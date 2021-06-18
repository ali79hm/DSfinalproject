from linkedlistclass import LinkedList

class Queue:
    
    def __init__(self,size):
        self.Queuedata = LinkedList()
        self.front = 0
        self.rear = 0
        self.max = size

    def getQueuedata(self):
        '''  return queue as list '''
        return self.Queuedata.getList()

    def getCount(self):
        '''  return count of list '''
        return len(self.Queuedata.getList())

    def Enqueue(self,data):
        '''  add data to queue 
             Enqueue(data)
        '''
        if self.rear != self.max:
            self.rear = self.rear+1
            self.Queuedata.InsertNode(data)
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
        else:
            #print("Queue is Empty")
            return -1
            

