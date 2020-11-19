def main():
    #instantiate linked list
    lst = LinkedList()
    while True:
        print('1. Add an item')
        print('2. Traverse linked list')
        print('3. Output all data')
        print('4. Reverse Traversal')
        print()
        print('5. Exit')

        choice = input('Enter choice: ')

        if choice == '1':
            print('---------')
            lst.AddNode()
            print('---------')

        elif choice == '2':
            print('---------')
            lst.Traversal()
            print('---------')

        elif choice == '3':
            print('---------------------------------------')
            lst.DisplayLinkedList()
            print('---------------------------------------')

        elif choice == '4':
            print('---------')
            lst.ReverseTraversal()
            print('---------')
            
        elif choice == '5':
            break




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
        self.Node = [ListNode() for i in range(31)]
        self.Start = 0
        self.NextFree = 1

        for i in range(1, 31):
            self.Node[i].setDataValue('')
            if i != 30:
                self.Node[i].setPointerValue(i+1)            
            

    def AddNode(self, NewItem):
        #NewItem = input('New Item: ')
        self.Node[self.NextFree].setDataValue(NewItem)  #change value of node

        #if linked list is empty
        if self.Start == 0:
            self.Start = self.NextFree #nextFree = 1
            Temp = self.Node[self.NextFree].getPointerValue()
            self.Node[self.NextFree].setPointerValue(0) #remove link of current node
            self.NextFree = Temp

        else:
            # traverse the list - starting at Start to find
            # the position at which to insert the new item
            Temp = self.Node[self.NextFree].getPointerValue()

            if NewItem < self.Node[self.Start].getDataValue():
                #new item will become the start of the list
                self.Node[self.NextFree].setPointerValue(self.Start)
                self.Start = self.NextFree
                self.NextFree = Temp

            else:
                #the new item is not at the start of the list
                Previous = 0
                Current = self.Start
                Found = False

                while not (Found or Current == 0):
                    if NewItem <= self.Node[Current].getDataValue():
                        self.Node[Previous].setPointerValue(self.NextFree)
                        self.Node[self.NextFree].setPointerValue(Current)
                        Found = True

                    else:
                        #move on to the next node
                        Previous = Current
                        Current = self.Node[Current].getPointerValue()

                if Current == 0:
                    self.Node[Previous].setPointerValue(self.NextFree)
                    self.Node[self.NextFree].setPointerValue(0)
                    self.NextFree = Temp
            

    def Traversal(self):
        self.TraversalInOrder(self.Start)

    def TraversalInOrder(self, Index):
        if Index != 0:
            print(self.Node[Index].getDataValue())
            self.TraversalInOrder(self.Node[Index].getPointerValue())

    def ReverseTraversal(self):
        self.ReverseTraversalInOrder(0)

    def ReverseTraversalInOrder(self, next_i):
        #check if last node
        for i in range(1, 31): 
            if self.Node[i].getPointerValue() == next_i:
                print(self.Node[i].getDataValue())
                self.ReverseTraversalInOrder(i)
                break
                

    def DisplayLinkedList(self):
        print('%-15s %-15s %-15s' %('Index', 'DataValue', 'Pointer'))
        for i in range(31):
              print('%-15s %-15s %-15s' %(i, self.Node[i].getDataValue(), self.Node[i].getPointerValue()))

    def IsEmpty(self):
        return self.Start == 0

    def isFull(self):
        for i in range(1, 31):
            if self.Node[i].getDataValue() == '':
                return False
        return True



lst = LinkedList()
lst.AddNode('MANGO')
lst.AddNode('ORANGE')
lst.AddNode('BANANA')
lst.AddNode('LEMON')
print(lst.DisplayLinkedList())
print('--------')
print('Traversal:')
print()
print(lst.Traversal())
print('--------')
print('Reverse Traversal:')
print()
print(lst.ReverseTraversal())
print(lst.isFull())

##main()
