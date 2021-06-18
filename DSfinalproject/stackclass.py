

class stack:
    maxSize = 100
    def __init__(self):
        self.topIndex = -1
        self.stackstorage = []

    def getstackdata(self):
        '''  return stack data as list '''
        return self.stackstorage
    
    def push(self,element):
        '''  push element to stack
             push(element)
        '''
        if self.topIndex >=(self.maxSize-1):
            #print("stack is full")
            return False
        else:
            self.topIndex = self.topIndex+1
            self.stackstorage.append(element)
            #print("pushed in stack!")
            return True

    def pop(self):
        '''  pop element from stack
             pop()
        '''
        if self.topIndex < 0:
            #print("stack is full")
            return False
        else:
           
            temp = self.stackstorage.pop(self.topIndex)
            self.topIndex = self.topIndex-1
            #print(f'{temp} poped into stack')
            return temp

    def peek(self):
        '''  fet top element of stack without removeing
             peek()
        '''
        if self.topIndex < 0:
            #print("stack is full")
            return False
        else:
            temp = self.stackstorage[self.topIndex]
            #print(f'{temp} is on top of into stack')
            return temp

    def isEmpty(self):
        '''  return True if stack is empty
             isEmpty()
        '''
        return self.topIndex < 0
    