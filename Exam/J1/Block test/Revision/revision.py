###CT1_TEMPLATE
from module import *
        
##construct stack class
####TASK 1.1#####  ##[total:6]
###implement your stack class here:
class Stack(LinkedList):
    def __init__(self):
        super().__init__()
    
    def push(self, value):
        self.add(value)
    
    def pop(self):
        currNode = self.root
        while currNode.getNext() != None:
            currNode = currNode.getNext()
        self.remove(currNode.getData())
        return currNode.getData()

##    def pop(self):
##        self.remove(self.root.getData())
##        return self.root

##class Stack:
##    def __init__(self):
##        self.s = []
##
##    def getSize(self):
##        return len(self.s)
##    
##    def push(self, value):
##        self.s.append(value)
##
##    def pop(self):
##        return self.s.pop()
##
##    def display(self):
##        return self.s


##a = Stack()
##for i in range(1, 6):
##    a.push(i)
##a.printList()
##a.pop()
##print()
##print()
##a.printList()
            

##########################################


##Node class given
class TreeNode:
    def __init__(self, Data):
        self.Data=Data
        self.LeftPtr=-1
        self.RightPtr=-1

    def getData(self):
        return self.Data

    def getLeftPtr(self):
        return self.LeftPtr

    def getRightPtr(self):
        return self.RightPtr

    def setLeftPtr(self,LeftP):
        self.LeftPtr=LeftP

    def setRightPtr(self,RightP):
        self.RightPtr=RightP


        


###################
class BinaryTree:
    def __init__(self):   
        self.ThisTree=[]
        self.Root=-1
        self.NextFreePosition=0

####TASK 1.2#####  ##[total:10]    
    ##implement you add method here:
    def add(self, value):
        newNode = TreeNode(value)
        
        if self.Root == -1:
            self.ThisTree.append(newNode)
            self.Root = 0
            self.NextFreePosition += 1
        
        else:
            currNode = self.ThisTree[self.Root]
            while True:
                if value > currNode.getData():
                    if currNode.getRightPtr() == -1:
                        self.ThisTree.append(newNode)
                        currNode.setRightPtr(self.NextFreePosition)
                        self.NextFreePosition += 1
                        break
                    else:
                        currNode = self.ThisTree[currNode.getRightPtr()]
                
                else:
                    if currNode.getLeftPtr() == -1:
                        self.ThisTree.append(newNode)
                        currNode.setLeftPtr(self.NextFreePosition)
                        self.NextFreePosition += 1
                        break
                    else:
                        currNode = self.ThisTree[currNode.getLeftPtr()]
    
    
    
    ##TASK 1.4######[total:6]
 ###implement InOrderTraversal method here:
    def InOrderTraversal(self):
        fringe = Stack()
        currIndex = 0
        currNode = self.ThisTree[currIndex]
        while not (currIndex == -1 and fringe.getSize() == 0):
            print()
            fringe.printList()
            print()
            if currIndex >= 0:
                currNode = self.ThisTree[currIndex]
##                print('currIndex:', currIndex)
##                print('currNode:', currNode.getData())
                fringe.push(currNode)
                currIndex = currNode.getLeftPtr()
            else:
                currNode = fringe.pop()
                print(currNode.getData())
                currIndex = currNode.getRightPtr()

                



##############################
    def display(self):
        if self.ThisTree==[]:
            return ("empty tree")
        print("{0:<8}{1:<12}{2:<8}{3:<8}".format("Index", "Data", "Left", "Right"))
        i=0    
        for node in self.ThisTree:
            print("{0:<8}{1:<12}{2:<8}{3:<8}".format(i, node.getData(),\
                                                node.getLeftPtr(),\
                                                  node.getRightPtr()))
            i+=1
           
        
        
        
#TASK 1.3#####  ##[total:3]        
###Write your commands here:
mrt = BinaryTree()
mrt.add('Marsiling')
mrt.add('Bishan')
mrt.add('Admiralty')
mrt.add('Tampines')
mrt.add('Punggol')
mrt.add('Jurong')
mrt.add('Yishun')
mrt.add('Woodlands')
mrt.add('Bedok')
mrt.display()
mrt.InOrderTraversal()
