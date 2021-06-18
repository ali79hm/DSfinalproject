class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

class LinkedList:
    def __init__(self):
        self.headnode = Node()
    def DisplayList(self):
        '''  print all nodes '''
        printval = self.headnode
        while printval is not None:
            print (printval.data)
            printval = printval.next

    def getList(self):
        '''  return all Nodes as a list '''
        getval = self.headnode
        mylist = []
        while getval is not None and getval.data!= None:
            mylist.append(getval.data)
            getval = getval.next
        return mylist

    def getNode(self,index = -1):
        '''  retun node with giving index '''
        currentIndex = 0
        currentNode = self.headnode
        if index == -1:
            while (currentNode.next != None):
                currentNode = currentNode.next
                currentIndex = currentIndex+1
        else:
            while (currentNode.next != None and currentIndex<index):
                currentNode = currentNode.next
                currentIndex = currentIndex+1
        return currentNode

    def IsEmpty(self):
        ''' return true if list is empty '''
        return self.headnode.data == None

    def InsertNode(self,data,index=-1):
        ''' usage : InsertNode(data(string),index(int))
            if index doesnt pass to function data will add to end
            for adding to first : index = 0
        '''
        currentIndex = 0
        currentNode = self.headnode
        newnode = Node(data)
        if self.headnode.data == None:
            self.headnode.data = data
        elif index==0: # add at first
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
        '''  delete node with given data '''
        currentNode = self.headnode
        previousNode = None
        while not(currentNode == None or currentNode.data ==  data):
            previousNode = currentNode
            currentNode = currentNode.next
        if currentNode != None:
            if previousNode == None:
                if currentNode.next==None:
                    self.headnode = Node()
                else:
                    self.headnode = currentNode.next
                currentNode = None
            else:
                previousNode.next = currentNode.next
                currentNode = None

    def DeleteNodewithindex(self,index = -1):
        '''  delete node with given index '''
        currentIndex = 0
        currentNode = self.headnode
        previousNode = None
        if currentNode.next == None and index==-1:
            index = 0

        if self.headnode.data == None:
            return -1
        elif index == -1:
            while (currentNode.next != None):
                previousNode = currentNode
                currentNode = currentNode.next;
            previousNode.next = None
            currentNode = None

        elif index == 0:
            if currentNode.next==None:
                self.headnode = Node()
            else:
                self.headnode = currentNode.next
            currentNode = None
        else:
            while (currentNode.next != None and currentIndex<index):
                previousNode = currentNode
                currentNode = currentNode.next
                currentIndex = currentIndex+1
            if currentIndex<index:
                pass
            else:
                previousNode.next = currentNode.next
                currentNode = None




