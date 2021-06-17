from linkedlistclass import LinkedList 

class stack:
    maxSize = 100
    def __init__(self):
        self.topIndex = -1
        #self.stackstorage = []
        self.stackstorage = LinkedList()

    def getstackdata(self):
        return self.stackstorage.getList()
        #return self.stackstorage
    
    def push(self,element):
        if self.topIndex >=(self.maxSize-1):
            #print("stack is full")
            return False
        else:
            self.topIndex = self.topIndex+1
            self.stackstorage.InsertNode(element)
            #self.stackstorage.append(element)
            #print("pushed in stack!")
            return True
    def pop(self):
        if self.topIndex < 0:
            #print("stack is full")
            return False
        else:
            temp = self.stackstorage.getNode()
            temp = temp.data
            self.stackstorage.DeleteNodewithindex()
            #temp = self.stackstorage.pop(self.topIndex)
            self.topIndex = self.topIndex-1
            #print(f'{temp} poped into stack')
            return temp
    def peek(self):
        if self.topIndex < 0:
            #print("stack is full")
            return False
        else:
            temp = self.stackstorage.getNode()
            temp = temp.data
            #temp = self.stackstorage[self.topIndex]
            #print(f'{temp} is on top of into stack')
            return temp
    def isEmpty(self):
        return self.topIndex < 0
