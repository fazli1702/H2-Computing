class Node:
    def __init__(self, data=''):
        self.data = data
        self.leftPtr = -1
        self.rightPtr = -1

    def getData(self):
        return self.data

    def getLeftPtr(self):
        return self.leftPtr

    def getRightPtr(self):
        return self.rightPtr

    def setData(self, new):
        self.data = new

    def setLeftPtr(self, new):
        self.leftPtr = new

    def setRightPtr(self, new):
        self.rightPtr = new

class Tree:
    def __init__(self):
        self.tree = []
        self.root = -1

    def add(self, newItem):
        nextFree = len(self.tree)
        newNode = Node(newItem)
        if self.root == -1:
            self.root = 0
            self.tree.append(newNode)
        
        else:
            curr = self.root
            while True:
                currNode = self.tree[curr]

                if newItem > currNode.getData():
                    if currNode.getRightPtr() == -1:
                        currNode.setRightPtr(nextFree)
                        self.tree.append(newNode)
                        break
                    else:
                        curr = currNode.getRightPtr()
                else:
                    if currNode.getLeftPtr() == -1:
                        currNode.setLeftPtr(nextFree)
                        self.tree.append(newNode)
                        break
                    else:
                        curr = currNode.getLeftPtr()

    def print(self):
        print('%-15s %-15s %-15s %-15s' % ('index', 'data', 'leftPtr', 'rightPtr'))
        for i in range(len(self.tree)):
            currNode = self.tree[i]
            print('%-15s %-15s %-15s %-15s' % (i, currNode.getData(), currNode.getLeftPtr(), currNode.getRightPtr()))


tree = Tree()
tree.add('Dave')
tree.add('Fred')
tree.add('Ed')
tree.add('Greg')
tree.add('Bob')
tree.add('Cid')
tree.add('Ali')
tree.print()
