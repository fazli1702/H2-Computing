def isOperator(s):
    return s in ['+', '-', '*', '/']


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

    def insert(self, newData, curr = 0, prev = 0):
        newNode = Node(newData)
        #empty tree
        if self.Root == -1:
            self.Root = 0
            self.Tree.append(newNode)
            self.NextFreeChild += 1

        else:
            currNode = self.Tree[curr]

            if isOperator(currNode.getData()):

                if currNode.getLeftChild() == -1:
                    self.Tree.append(newNode)
                    currNode.setLeftChild(self.NextFreeChild)
                    self.NextFreeChild += 1

                elif currNode.getRightChild() == -1:
                    self.Tree.append(newNode)
                    currNode.setRightChild(self.NextFreeChild)
                    self.NextFreeChild += 1

                else:
                    if isOperator(self.Tree[currNode.getLeftChild()].getData()):
                        prev = curr
                        curr = currNode.getLeftChild()
                        self.insert(newData, curr, prev)

                    elif isOperator(self.Tree[currNode.getRightChild()].getData()):
                        prev = curr
                        curr = currNode.getRightChild()
                        self.insert(newData, curr, prev)

                    else:
                        curr = self.Tree[prev].getRightChild()
                        self.insert(newData, curr, prev)


    def insertIter(self, newData):
        
        newNode = Node(newData)
        
        if self.Root == -1:  #empty tree
            self.Root = 0
            self.Tree.append(newNode)
            self.NextFreeChild += 1

        else:
            curr = self.Root
            prev = self.Root
            while True:
                currNode = self.Tree[curr]
                
                if isOperator(currNode.getData()):
                    if currNode.getLeftChild() == -1:
                        self.Tree.append(newNode)
                        currNode.setLeftChild(self.NextFreeChild)
                        self.NextFreeChild += 1
                        break
                    
                    elif currNode.getRightChild() == -1:
                        self.Tree.append(newNode)
                        currNode.setRightChild(self.NextFreeChild)
                        self.NextFreeChild += 1
                        break
                    
                    else:
                        if isOperator(self.Tree[currNode.getLeftChild()].getData()):
                            prev = curr
                            curr = currNode.getLeftChild()

                        elif isOperator(self.Tree[currNode.getRightChild()].getData()):
                            prev = curr
                            curr = currNode.getRightChild()

                        else:
                            curr = self.Tree[prev].getRightChild()
                            

    def infix1(self, curr = 0):
        currNode = self.Tree[curr]
        string = ''

        if self.Root == -1:
            return 'Empty tree'

        else:
            # traverse left sub tree
            if currNode.getLeftChild() != -1:
                if curr == 0:
                    string += self.infix(currNode.getLeftChild())
                else:
                    string += '(' + self.infix(currNode.getLeftChild())
                    
            # current Node
            string += currNode.getData()
            # traverse right sub tree
            if currNode.getRightChild() != -1:
                if curr == 0:
                    string += self.infix(currNode.getRightChild())
                else:
                    string += self.infix(currNode.getRightChild()) + ')'


        return string



    def infix(self, n = 0):
        if n == -1:
            return ''
            
        left = self.infix(self.Tree[n].getLeftChild())
        right = self.infix(self.Tree[n].getRightChild())
        
        if isOperator(self.Tree[self.Tree[n].getLeftChild()].getData()):
            left = '(' + left + ')'
            
        if isOperator(self.Tree[self.Tree[n].getRightChild()].getData()):
            right = '(' + right + ')'
            
        return left + self.Tree[n].getData() + right




    def display(self):
        print('%-15s %-15s %-15s %-15s' % ('Index', 'Data', 'LeftChild', 'RightChild'))
        for i in range(len(self.Tree)):
            print('%-15s %-15s %-15s %-15s' % (i, self.Tree[i].getData(), self.Tree[i].getLeftChild(),
                self.Tree[i].getRightChild()))





#################
print('expected infix output: (2 * 4) + (3 - 1)')
print('tree1:')
tree1 = ExpressionTree()
tree1.insert('+')
tree1.insert('*')
tree1.insert('-')
tree1.insert('2')
tree1.insert('4')
tree1.insert('3')
tree1.insert('1')
tree1.display()
print()
print('infix:', tree1.infix())
print()


#################
print('tree2:')
3 + (4 / 2)
tree2 = ExpressionTree()
tree2.insert('+')
tree2.insert('3')
tree2.insert('/')
tree2.insert('4')
tree2.insert('2')
tree2.display()
print()
print('infix:', tree2.infix())
print()



# #################
print('tree3:')
(2 * (3 + 1)) + 4
tree3 = ExpressionTree()
tree3.insert('+')
tree3.insert('*')
tree3.insert('4')
tree3.insert('2')
tree3.insert('+')
tree3.insert('3')
tree3.insert('1')
tree3.display()
print()
print('infix:', tree3.infix())

