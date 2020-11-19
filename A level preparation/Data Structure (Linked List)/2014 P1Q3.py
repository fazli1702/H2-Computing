class ListNode:
    def __init__(self):
        self.DataValue = ''
        self.PointerValue = 0

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
        self.Start = 0
        self.NextFree = 1
        self.Node = [ListNode() for i in range(31)]
        for i, node in enumerate(self.Node):
            if i == 0:
                self.Node[i] = None
            else:
                if i < 30:
                    node.setPointerValue(i+1)
                node.setDataValue('')


    def AddNode(self, NewItem):
        # NewItem = input('NewItem:')
        self.Node[self.NextFree].setDataValue(NewItem) 

        if self.Start == 0:
            self.Start = self.NextFree
            Temp = self.Node[self.NextFree].getPointerValue()
            self.Node[self.NextFree].setPointerValue(0)
            self.NextFree = Temp

        else:
            # traverse the list – starting at Start to find
            # the position at which to insert the new item
            Temp = self.Node[self.NextFree].getPointerValue()

            if NewItem < self.Node[self.Start].getDataValue():
                # new item wll become the start of the list
                self.Node[self.NextFree].PointerValue = self.Start
                self.Start = self.NextFree
                self.NextFree = Temp

            else:
                # new item not at start of list
                Previous = 0
                Current = self.Start # 1
                Found = False

                while not (Found or Current == 0):
                    if NewItem <= self.Node[Current].getDataValue():
                        self.Node[Previous].setPointerValue(self.NextFree)
                        self.Node[self.NextFree].setPointerValue(Current)
                        self.NextFree = Temp
                        Found = True

                    else:
                        # move to next node
                        Previous = Current
                        Current = self.Node[Current].getPointerValue()

                if Current == 0:
                    self.Node[Previous].setPointerValue(self.NextFree)
                    self.Node[self.NextFree].setPointerValue(0)
                    self.NextFree = Temp

        

    def Traversal(self):
        return self.TraversalInOrder(self.Start)

    def TraversalInOrder(self, Index):
        if Index != 0:
            print(self.Node[Index].getDataValue())
            self.TraversalInOrder(self.Node[Index].getPointerValue())




    def ReverseTraversal(self):
        return self.TraversalInReverseOrder(self.Start)

    def TraversalInReverseOrder(self, Index, lst=[]):
        if Index != 0:
            lst.append(self.Node[Index].getDataValue())
            self.TraversalInReverseOrder(self.Node[Index].getPointerValue())
        else:
            for i in range(len(lst)-1, -1, -1):
                print(lst[i])


    def DisplayLinkedList(self):
        print('Start:', self.Start)
        print('NextFree:', self.NextFree)
        print('%-15s %-15s %-15s' % ('index', 'DataValue', 'PointerValue'))
        for i in range(1, 31):
            node = self.Node[i]
            print('%-15s %-15s %-15s' % (i, node.getDataValue(), node.getPointerValue()))

    def IsEmpty(self):
        return self.Start == 0

    def IsFull(self):
        return self.NextFree > 30




def main():
    test = ['MANGO', 'ORANGE', 'BANANA', 'LEMON']
    lst = LinkedList()
    for ele in test:
        lst.AddNode(ele)
    lst.DisplayLinkedList()
    lst.Traversal()
    lst.ReverseTraversal()
    # while True:
    #     print('1. Add an item')
    #     print('2. Display used nodes')
    #     print('3. Dislpay whole linked list')
    #     print('5. Exit')

    #     choice = input('Enter choice:')

    #     if choice == '1':
    #         newItem = input('Enter new item:')
    #         lst.AddNode(newItem)

    #     if choice == '2':
    #         lst.Traversal()

    #     if choice == '3':
    #         lst.DisplayLinkedList()

    #     if choice == '5':
    #         break
main()


