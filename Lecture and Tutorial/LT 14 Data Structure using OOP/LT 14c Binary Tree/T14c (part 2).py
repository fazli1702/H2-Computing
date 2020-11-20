class ConnectionNode:
    def __init__(self):
        self.DataValue = ''
        self.LeftChild = 0
        self.RightChild = 0

    def getDataValue(self):
        return self.DataValue

    def getLeftChild(self):
        return self.LeftChild

    def getRightChild(self):
        return self.RightChild

    def setDataValue(self, newData):
        self.DataValue = newData

    def setLeftChild(self, newLeftChild):
        self.LeftChild = newLeftChild

    def setRightChild(self, newRightChild):
        self.RightChild = newRightChild



class LinkedList:
    def __init__(self):
        self.RobotData = [ConnectionNode() for i in range(26)]
        self.Root = 1
        self.NextFreeChild = 1

        for i in range(1, 25):
            self.RobotData[i].setLeftChild(i+1)
            

    def FindNode(self, NodeValue):
        Found = False
        curr_i = self.Root
        
        while not (Found or curr_i > 25):
            #print(curr_i)
            if self.RobotData[curr_i].getDataValue() == NodeValue:
                Found = True
            else:
                curr_i += 1

        if curr_i > 25:
            return 0
        else:
            return curr_i
        

    def AddToRobotData(self, NewDataItem, ParentItem, ThisMove):
        #print('self.NextFreeChild:', self.NextFreeChild)
        
        #if bst is empty
        if self.Root == 1 and self.NextFreeChild == 1:
            #print('case 1 executed, "{}" added'.format(NewDataItem))
            self.NextFreeChild = self.RobotData[self.NextFreeChild].getLeftChild()
            self.RobotData[self.Root].setLeftChild(0)
            self.RobotData[self.Root].setDataValue(NewDataItem)

        else:
            #check if parent exist
            ParentPosition = self.FindNode(ParentItem)  #index value:int

            if ParentPosition > 0:  #parent exist
                #check if child exist
                ExistingChild = self.FindNode(NewDataItem)
                
                if ExistingChild > 0:  #child exist
                    #print('case 2 executed, "{}" added'.format(NewDataItem))
                    ChildPointer = ExistingChild
                    
                else:
                    #print('case 3 executed, "{}" added'.format(NewDataItem))
                    ChildPointer = self.NextFreeChild
                    self.NextFreeChild = self.RobotData[self.NextFreeChild].getLeftChild()  #update next free child value
                    self.RobotData[ChildPointer].setLeftChild(0)  #delink from other node
                    self.RobotData[ChildPointer].setDataValue(NewDataItem)  #set node value

                if ThisMove == 'L':
                    self.RobotData[ParentPosition].setLeftChild(ChildPointer)
                else:
                    self.RobotData[ParentPosition].setRightChild(ChildPointer)

        
    def PreOrder(self, curr_i = 1, path = ''):
        #N, L, R
        current = self.RobotData[curr_i]
        #empty bst
        if self.Root == 1 and self.NextFreeChild == 1:
            return 'Empty Tree'

        elif current.getDataValue() == 'Z':
            print(path+ 'Z')

        
        #check if leaf node
        elif current.getLeftChild() == 0 and current.getRightChild() == 0:
            #print(current.getDataValue())
            path += current.getDataValue() + ' -> '


        else:
            #node
            #print(current.getDataValue())
            path += current.getDataValue() + ' -> '

            #traverse left sub tree
            if current.getLeftChild() != 0:
                curr_i = current.getLeftChild()
                self.PreOrder(curr_i, path)

            #traverse right sub tree
            if current.getRightChild() != 0:
                curr_i = current.getRightChild()
                self.PreOrder(curr_i, path)




    def OutputData(self):
        print('root:', self.Root)
        print('Next Free Child:', self.NextFreeChild)
        print('----------------------------------------------------------')
        print("%-15s %-15s %-15s %s" %('Index', 'DataValue', 'LeftChild', 'RightChild'))
        for i in range(1, len(self.RobotData)):
            print("%-15s %-15s %-15s %s" %(i, self.RobotData[i].getDataValue(), self.RobotData[i].getLeftChild(),
                    self.RobotData[i].getRightChild()))


                
                


##a = LinkedList()
##a.AddToRobotData('A', 0, 'X')
##a.AddToRobotData('B', 'A', 'L')
##a.AddToRobotData('D', 'A', 'R')
##print(a.OutputData())



def main():
    #read txt file
    f = open('SEARCHTREE.txt', 'r')
    lst = LinkedList()
    for ele in f:
        #print(ele[0], ele[2], ele[4])
        lst.AddToRobotData(ele[0], ele[2], ele[4])
    #lst.OutputData()
    lst.PreOrder()

main()











#end
###########################################################

#another method to read txt file
def main2():
    a = LinkedList()
    file = open('SEARCHTREE.txt')
    lines = file.readline()
    for line in lines:
        #print(line.strip())#.split(','))
        [NewDataItem, ParentItem, ThisMove] = line.strip().split(',')
        #print(NewDataItem, ParentItem, ThisMove)
        a.AddToRobotData(NewDataItem, ParentItem, ThisMove)
    a.OuputData()

##main2()
