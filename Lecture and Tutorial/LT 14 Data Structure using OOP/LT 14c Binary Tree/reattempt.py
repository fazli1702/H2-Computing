def isOperator(n):
	return n in ['+', '-', '*', '/']

class Node:
    def __init__(self,data):
        self.Data=data
        self.LeftChild=-1
        self.RightChild=-1

    def getData(self):
        return self.Data

    def getLeftChild(self):
        return self.LeftChild

    def getRightChild(self):
        return self.RightChild

    def setData(self,new):
        self.Data=new

    def setLeftChild(self,new):
        self.LeftChild = new

    def setRightChild(self,new):
        self.RightChild=new


class ExpressionTree:
    def __init__(self):
        self.Tree = []
        self.Root = -1
        self.NextFreeChild = 0

    def insert(self, newData):
    	newNode = Node(newData)

    	if self.Root == -1:
    		self.Root = 0
    		self.Tree.append(newNode)
    		self.NextFreeChild += 1

    	else:
    		curr = self.Root
    		prev = []
    		while True:
    			currNode = self.Tree[curr]

    			if isOperator(currNode.getData()):

    				if currNode.getLeftChild() == -1:
    					currNode.setLeftChild(self.NextFreeChild)
    					self.Tree.append(newNode)
    					self.NextFreeChild += 1
    					break

    				elif currNode.getRightChild() == -1:
    					currNode.setRightChild(self.NextFreeChild)
    					self.Tree.append(newNode)
    					self.NextFreeChild += 1
    					break

    				else:
    					if isOperator(self.Tree[currNode.getLeftChild()].getData()):
    						prev.append(curr)
    						curr = currNode.getLeftChild()

    					elif isOperator(self.Tree[currNode.getRightChild()].getData()):
    						prev.append(curr)
    						curr = currNode.getRightChild()

    					else:
    						curr = prev.pop(0)

    			else:
    				print('cannot be inserted')
    				break

