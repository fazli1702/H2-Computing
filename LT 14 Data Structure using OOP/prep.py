class ListNode:
    def __init__(self, DataValue='', PointerValue=0):
        self.DataValue = DataValue
        self.PointerValue = PointerValue

    def getDataValue(self):
        return self.DataValue

    def getPointerValue(self):
        return self.PointerValue

    def setDataValue(self, new):
        self.DataValue = new

    def setPointerValue(self, new):
        self.PointerValue = new


class LinkedList:
    def __init__(self):
        self.Node = [ListNode('', i+1) for i in range(31)]
        self.Node[-1].setPointerValue(0)
        self.Start = 0
        self.NextFree = 1


    def AddNode(self, value):
        if self.Start == 0:
            self.Node[self.NextFree].setDataValue(value)
            self.Node[self.NextFree].setPointerValue(0)
            self.Start = 1

        else:
            pass
    

    def DisplayLinkedList(self):
        print('Start:', self.Start)
        print('NextFree:', self.NextFree)
        print()
        print('%-15s %-15s %-15s' % ('Index', 'DataValue', 'PointerValue'))
        for i in range(1, len(self.Node)):
            print('%-15s %-15s %-15s' % (i, self.Node[i].getDataValue(), self.Node[i].getPointerValue()))



fruits = LinkedList()
fruits.AddNode('BANANA')
fruits.DisplayLinkedList()
            
