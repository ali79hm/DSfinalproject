class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

class LinkedList:
    def __init__(self):
        #self.headval = None
        self.headnode = Node()
    def DisplayList(self):
        printval = self.headnode
        while printval is not None:
            print (printval.data)
            printval = printval.next

    def getList(self):
        '''  return all Nodes as a list '''
        getval = self.headnode
        mylist = []
        while printval is not None:
            mylist.append(getval.data)
            getval = getval.next
        return mylist

    def IsEmpty(self):
        ''' return true if list is empty '''
        return self.headnode.data == None

    def InsertNode(self,data,index=None):
        ''' usage : InsertNode(data(string),index(int))
            if index doesnt pass to function data will add to first
            for adding to end : index = -1
        '''
        currentIndex = 0
        currentNode = self.headnode
        newnode = Node(data)
        if self.headnode.data == None:
            self.headnode.data = data
        elif index == None or index==0: # add at first
            newnode.next = self.headnode
            self.headnode = newnode
        elif index == -1:               # add to end
            while (currentNode.next != None):
                currentNode = currentNode.next;
            newnode = Node(data)
            currentNode.next = newnode
        else:                         # add with index
            while (currentNode.next != None and currentIndex<index-1):
                currentNode = currentNode.next
                currentIndex = currentIndex+1
            newnode = Node(data)
            newnode.next = currentNode.next
            currentNode.next = newnode


    def DeleteNode(self,data):
        currentNode = self.headnode
        previousNode = None
        while not(currentNode == None or currentNode.data ==  data):
            previousNode = currentNode
            currentNode = currentNode.next
        if currentNode != None:
            if previousNode == None:
                self.headnode = currentNode.next
                currentNode = None
            else:
                previousNode.next = currentNode.next
                currentNode = None


