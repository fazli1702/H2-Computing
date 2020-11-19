## DO NOT modify or delete any code provide in this module.
## (JC2 Common Test 1 - 21 Feb 2019)

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def getNext(self):
        return self.next
  
    def setNext(self, next):
        self.next = next
   
    def getData(self):
        return self.data
  
    def setData(self, data):
        self.data = data

    def toString(self):
        print('Node value: ' + str(self.data.getData()))
        
        
class LinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size=0

    def getSize(self):          # returns size of linkedlist
        return self.size  
  
    def add(self, data):          # add a node to the front of the linked list
        new_node = Node(data, self.root)
        self.root = new_node
        self.size+=1
    
  
    def remove(self, data):   # remove a node from the front of the linked list
        this_node = self.root
        prev_node = None
        self.size-=1
        while this_node:     # equivalent to while this_node != None
            if this_node.getData() == data:
                if prev_node:        # equivalent to prev_node != None:
                    prev_node.setNext(this_node.getNext())
                else:
                    self.root = this_node.getNext()
                return True
            else:
                prev_node = this_node
                this_node = this_node.getNext()
        
        return False
  
    
    def printList(self):    # print only non-empty list
        if self.root != None:
            this_node = self.root
            while this_node:
                this_node.toString()
                this_node = this_node.getNext()
