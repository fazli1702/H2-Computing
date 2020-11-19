class Node:
    def __init__(self, Data=''):
        self.Data = Data
        self.LeftPtr = 0
        self.RightPtr = 0
        
    def getData(self):
        return self.Data
    
    def getLeftPtr(self):
        return self.LeftPtr
    
    def getRightPtr(self):
        return self.RightPtr
    
    def setData(self, new):
        self.Data = new
        
    def setLeftPtr(self, new):
        self.LeftPtr = new
        
    def setRightPtr(self, new):
        self.RightPtr = new
        
        
        
class DataStructure:
    def __init__(self):
        self.TreeData = [Node() for i in range(21)]
        self.Root = 0
        self.NextFree = 1
        for i in range(1, 20):
            self.TreeData[i].setLeftPtr(i+1)
            
    def add(self, value):
        
        if self.Root == 0:
            self.TreeData[self.NextFree].setData(value)
            self.TreeData[self.NextFree].setLeftPtr(0)
            self.Root = 1
            self.NextFree += 1
            
            
        else:
            self.TreeData[self.NextFree].setData(value)
            self.TreeData[self.NextFree].setLeftPtr(0)
            curr = self.Root
            while True:    
                currNode = self.TreeData[curr]
                if value < currNode.getData():
                    if currNode.getLeftPtr() == 0:
                        currNode.setLeftPtr(self.NextFree)
                        self.NextFree += 1
                        break
                    else:
                        curr = currNode.getLeftPtr()
                
                else:
                    if currNode.getRightPtr() == 0:
                        currNode.setRightPtr(self.NextFree)
                        self.NextFree += 1
                        break
                    else:
                        curr = currNode.getRightPtr()
                        
                        
    def Traversal(self, curr=1):
        if self.Root == 0:
            return None

        else:
            currNode = self.TreeData[curr]
##            if currNode.getLeftPtr() == 0 and currNode.getRightPtr() == 0:
##                print(currNode.getData())

       
            if currNode.getLeftPtr() != 0:
                self.Traversal(currNode.getLeftPtr())

            print(currNode.getData())

            if currNode.getRightPtr() != 0:
                self.Traversal(currNode.getRightPtr())
                    
                
            
            
    def display(self):
        print('Root:', self.Root)
        print('NextFree:', self.NextFree)
        print()
        print('%-15s %-15s %-15s %-15s' % ('Index', 'Data', 'LeftPtr', 'RightPtr'))
        for i in range(1, 21):
            print('%-15s %-15s %-15s %-15s' % (i, self.TreeData[i].getData(), self.TreeData[i].getLeftPtr(), self.TreeData[i].getRightPtr()))
            


tree = DataStructure()
tree.add('monkey')
tree.add('football')
tree.add('qwerty123')
tree.add('yijc123')
tree.add('p@ssword')
tree.add('letmepass')
tree.add('asdfgh')
##tree.display()
print()
tree.Traversal()




