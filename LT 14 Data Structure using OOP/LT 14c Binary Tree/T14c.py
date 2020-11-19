#q1

#####Node class#######

class Node:
    def __init__(self):
        self.data = ''
        self.leftPtr = -1
        self.rightPtr = -1

    def getData(self):
        return self.data

    def getLeftPtr(self):
        return self.leftPtr

    def getRightPtr(self):
        return self.rightPtr

    def setData(self, newData):
        self.data = newData

    def setLeftPtr(self, newLeft):
        self.leftPtr = newLeft

    def setRightPtr(self, newRight):
        self.rightPtr = newRight


#######Tree class#######
        
class Tree:
    def __init__(self):
        self.tree = []
        self.root = -1
        self.next_position = 0

    def add(self, newItem, curr_i = 0):  # newItem: string
        newNode = Node()
        newNode.setData(newItem)

        #if empty tree, update root
        if self.root == -1:
            self.root = 0
            self.next_position += 1
            self.tree.append(newNode)

        else:
            current = self.tree[curr_i]  #node object

            #compare data of newNode and current
            #add to left sub tree
            if newItem <= current.getData():
                if current.getLeftPtr() == -1:
                    self.tree.append(newNode)
                    current.setLeftPtr(self.next_position)
                    self.next_position += 1
                else:
                    self.add(newItem, current.getLeftPtr())
                    
            #add to right sub tree
            else:
                if current.getRightPtr() == -1:
                    self.tree.append(newNode)
                    current.setRightPtr(self.next_position)
                    self.next_position += 1
                else:
                    self.add(newItem, current.getRightPtr())


    def inOrderTraversal(self, curr_i = 0):
        if self.root == -1:
            return 'Empty Tree'

        current = self.tree[curr_i]

        if current.getLeftPtr() == -1 and current.getRightPtr() == -1:
            print(current.getData())

        else:
            if current.getLeftPtr() != -1:
                curr_i = current.getLeftPtr()
                self.inOrderTraversal(curr_i)

            print(current.getData())

            if current.getRightPtr() != -1:
                curr_i  = current.getRightPtr()
                self.inOrderTraversal(curr_i)
        
        

    def print(self):
        for i in range(len(self.tree)):
            print('index:', i, '\tdata:', self.tree[i].getData(),
                  '\tleftPtr:', self.tree[i].getLeftPtr(), '\trightPtr:',
                  self.tree[i].getRightPtr())



##t1 = Tree()
##t1.add("Dave")
##t1.add("Fred")
##t1.add("Ed")
##t1.add("Greg")
##t1.add("Bob")
##t1.add("Cid")
##t1.add("Ali")
##print(t1.print())
##print(t1.inOrderTraversal())






