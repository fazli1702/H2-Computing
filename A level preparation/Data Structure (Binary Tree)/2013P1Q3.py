class Node:
    def __init__(self):
        self.Data = ''
        self.LeftP = 0
        self.RightP = 0

    def getData(self):
        return self.Data

    def getLeftP(self):
        return self.LeftP

    def getRightP(self):
        return self.RightP

    def setData(self, new):
        self.Data = new

    def setLeftP(self, new):
        self.LeftP = new

    def setRightP(self, new):
        self.RightP = new



class BinaryTree:
    def __init__(self):
        self.root = 0
        self.NextFreePosition = 1
        self.ThisTree = [Node() for i in range(21)]
        for i in range(1, 20):
            self.ThisTree[i].setLeftP(i+1)

    # task 3.2
    def AddItemToBinaryTree(self, NewTreeItem):
        if self.root == 0:
            self.root = self.NextFreePosition
            self.ThisTree[self.root].setData(NewTreeItem)
            self.ThisTree[self.root].setLeftP(0)
            self.NextFreePosition += 1

        # check for available space for new item
        elif self.NextFreePosition > 20:
            return None

        else:
            # traverse tree
            CurrentPosition = self.root
            LastMove = 'X'
            while CurrentPosition != 0:
                PreviousPosition = CurrentPosition
                if NewTreeItem < self.ThisTree[CurrentPosition].getData():
                    # move left
                    LastMove = 'L'
                    CurrentPosition = self.ThisTree[CurrentPosition].getLeftP()
                else:
                    # move right
                    LastMove = 'R'
                    CurrentPosition = self.ThisTree[CurrentPosition].getRightP()

            if LastMove == 'R':
                self.ThisTree[PreviousPosition].setRightP(self.NextFreePosition)
                self.ThisTree[self.NextFreePosition].setData(NewTreeItem)
            else:
                self.ThisTree[PreviousPosition].setLeftP(self.NextFreePosition)
                self.ThisTree[self.NextFreePosition].setData(NewTreeItem)

            temp = self.NextFreePosition
            self.NextFreePosition = self.ThisTree[self.NextFreePosition].getLeftP()
            self.ThisTree[temp].setLeftP(0)


    # task 3.6
    def InOrderTraversal(self, currIndex=1):
        if self.root == 0:
            return 'Empty Tree'

        currNode = self.ThisTree[currIndex]
        # leaf/child node
        if currNode.getRightP() == 0 and currNode.getLeftP() == 0:
            print(currNode.getData())

        else:
            if currNode.getLeftP() != 0:
                i = currNode.getLeftP()
                self.InOrderTraversal(i)

            print(currNode.getData())

            if currNode.getRightP() != 0:
                i = currNode.getRightP()
                self.InOrderTraversal(i)

            
                
    # task 3.3
    def OutputData(self):
        print('root:', self.root)
        print('NextFreePosition:', self.NextFreePosition)
        print('%-15s %-15s %-15s %-15s' % ('index', 'data', 'leftP', 'rightP'))
        for i in range(1, 21):
            node = self.ThisTree[i]
            print('%-15s %-15s %-15s %-15s' % (i, node.getData(),
                                               node.getLeftP(), node.getRightP()))





# task 3.4
def main():
    # task 3.5
    test = ['INDIA', 'NEPAL', 'MALAYSIA', 'SINGAPORE', 'BURMA',  'CANADA', 'LATVIA', 'XXX']
    tree = BinaryTree()
    i = 0
    while True:
        # newItem = input('Enter new item:')
        newItem = test[i]
        if newItem.upper() == 'XXX':
            break
        else:
            tree.AddItemToBinaryTree(newItem)
        i += 1

    tree.OutputData()
    tree.InOrderTraversal()
  
main()