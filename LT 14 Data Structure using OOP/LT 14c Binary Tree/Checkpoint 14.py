def isOperator(s):
    for ele in '+-*/':
        if s == ele:
            return True
    return False


####DO NOT remove/modify###############
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
        self.LeftChild=new

    def setRightChild(self,new):
        self.RightChild=new
        
###################################################################
######Your ExpressionTree class here: ##############################
###########################################################
        
class ExpressionTree:
    def __init__(self):
        self.Tree = []
        self.Root = -1
        self.NextFreeChild = 0

    def insert(self, newData, curr_i = 0):
        newNode = Node(newData)
        #empty bst
        if self.Root == -1:            
            if isOperator(newData):
                self.Root = 0
                self.Tree.append(newNode)
                self.NextFreeChild += 1

        else:
            current = self.Tree[curr_i]
            if isOperator(current.getData()):
                
                if current.getLeftChild() == -1:
                    print('option 1')
                    self.Tree.append(newNode)
                    current.setLeftChild(self.NextFreeChild)
                    self.NextFreeChild += 1

                elif current.getRightChild() == -1:
                    print('option 2')
                    self.Tree.append(newNode)
                    current.setRightChild(self.NextFreeChild)
                    self.NextFreeChild += 1

                else:
                    if isOperator(self.Tree[current.getLeftChild()].getData()):
##                        print('option 3')
                        self.insert(current.getLeftChild())

                    elif isOperator(self.Tree[current.getRightChild()].getData()):
##                        print('option 4')
                        self.insert(current.getRightChild())
                
                
                    


    def inOrder(self, curr_i = 0):
        current = self.Tree[curr_i]

        if current.getLeftChild() == -1 and current.getRightChild == -1:
            print(current.getData())

        else:
            if current.getLeftChild() != -1:
                curr_i = current.getLeftChild()
                self.inOrder(curr_i)

            print(current.getData())

            if current.getRightChild() != -1:
                curr_i = current.getRightChild()
                self.inOrder(curr_i)
            
        

    def display(self):
        print('root:', self.Root)
        print('NextFreeChild:', self.NextFreeChild)
        print()
        print('%-15s %-15s %-15s %-15s' % ('Index', 'Data', 'LeftChild', 'RightChild'))
        for i in range(len(self.Tree)):
            print('%-15s %-15s %-15s %-15s' % (i, self.Tree[i].getData(), self.Tree[i].getLeftChild(),
                                               self.Tree[i].getRightChild()))



tree1=ExpressionTree()
tree1.insert('+')
tree1.insert('*')
tree1.insert('4')
tree1.insert('2')
tree1.insert('+')
tree1.insert('3')
tree1.insert('1')

tree1.display()
