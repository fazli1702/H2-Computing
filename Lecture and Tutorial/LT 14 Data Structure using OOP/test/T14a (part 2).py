def main():
    while True:
        print('1. Add item')
        print('2. Traverse linked list')
        print('3. Ouput all data')
        print()
        print('5. Exit')

        choice = input('Enter your choice:')

        if choice == '1':
            pass

        elif choice == '2':
            pass

        elif choice == '3':
            pass

        elif choice == '5':
            break

        else:
            print('Please enter a valid choice')



class ListNode:
    def __init__(self):
        self.DataValue = ''
        self.PointerValue = 0  #-1 or None 

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
        self.Node = [ListNode() for i in range(31)]  # append node into array
        self.Start = 1
        self.NextFree = 1

        # link all nodes together
        # change DataValue to 'empty string'
        for i in range(1, 31):
            if i != 30:
                self.Node[i].setPointerValue(i+1)


    def AddNode(self, value):
        # add value to empty linked list
        if self.IsEmpty():
            print('option 1')
            self.Node[self.NextFree].setDataValue(value)
            self.Node[self.NextFree].setPointerValue(0)
            self.NextFree += 1

        else:
            # add value at start of linked list
            if value < self.Node[self.Start].getDataValue():
                print('option 2')
                self.Node[self.NextFree].setDataValue(value)
                self.Node[self.NextFree].setPointerValue(self.Start)
                self.Start = self.NextFree
                self.NextFree += 1
                return None
                
            # traverse through linked list
            prev = 0
            curr = self.Start
            currNode = self.Node[curr]
            while value > currNode.getDataValue() and currNode.getDataValue() != '':
                prev = curr
                curr += 1
                currNode = self.Node[curr]

            if currNode.getDataValue() == '':
                print('option 3')
                # add data value at end of linked list
                currNode.setDataValue(value)
                currNode.setPointerValue(0)
                self.Node[prev].setPointerValue(self.NextFree)
                self.NextFree += 1

            else:
                # add data in b/w nodes
                print('option 4')
                print('prev:', prev)
                print('curr:', curr)
                self.Node[prev].setPointerValue(self.NextFree)
                self.Node[self.NextFree].setDataValue(value)
                self.Node[self.NextFree].setPointerValue(curr)
                self.NextFree += 1
                


    def Traversal(self):
        self.TraversalInOrder(self.Start)

    def TraversalInOrder(self, curr_i):
        if curr_i != 0:
            print(self.Node[curr_i].getDataValue())
            curr_i = self.Node[curr_i].getPointerValue()
            self.TraversalInOrder(curr_i)

    def ReverseTraversal(self):
        self.ReverseTraversalInOrder(0)

    def ReverseTraversalInOrder(self, next_i):
        for i in range(1, len(self.Node)):
            if self.Node[i].getPointerValue() == next_i:
                print(self.Node[i].getDataValue())
                self.ReverseTraversalInOrder(i)
                break

    def DisplayLinkedList(self):
        print('Start:', self.Start)
        print('Next Free:', self.NextFree)
        print()
        print('%-10s %-10s %-10s' % ('Index','DataValue', 'PointerValue'))
        for i in range(1, len(self.Node)):
            print('%-10s %-10s %-10s' % (i, self.Node[i].getDataValue(), self.Node[i].getPointerValue()))
        

    def IsEmpty(self):
        return self.NextFree == 1

    def IsFull(self):
        pass
    
    
        
lst = LinkedList()
lst.AddNode('MANGO')
lst.AddNode('ORANGE')
lst.AddNode('PEAR')
lst.AddNode('BANANA')
lst.AddNode('APPLE')
# lst.AddNode('LEMON')
lst.DisplayLinkedList()
print()
lst.Traversal()
print()
lst.ReverseTraversal()
