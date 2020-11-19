# Task 3.1
class ListNode:
    def __init__(self):
        self.Name = ''
        self.Pointer = 0
    
    def SetName(self, Name):
        self.Name = Name
        
    def SetPointer(self, Pointer):
        self.Pointer = Pointer
        
    def GetName(self):
        return self.Name
    
    def GetPointer(self):
        return self.Pointer
    
    
class LinkedList:
    def __init__(self):
        self.Node = [ListNode() for i in range(11)]
        self.Start = 0
        self.NextFree = 1
        for i in range(10):
            if i == 0:
                self.Node[i] = None
            else:
                self.Node[i].SetPointer(i+1)
                
    def Insert(self, name, position):
        newNode = self.Node[self.NextFree]
        newNode.SetName(name)
        Temp = self.Node[self.NextFree].GetPointer()
        
        if position == 1:
            newNode.SetPointer(self.Start)
            self.Start = self.NextFree
            self.NextFree = Temp
            
        else:
            prev = self.Start
            curr = self.Node[prev].GetPointer()
            for i in range(1, position-1):
                prev = curr
                curr = self.Node[curr].GetPointer()                
            self.Node[prev].SetPointer(self.NextFree)
            self.Node[self.NextFree].SetPointer(curr)
            self.NextFree = Temp
                
                
    def Delete(self, position):
        if self.Start == 0:
            return 'Cannot delete from empty linked list'
        
        elif position == 1:
            self.Node[self.Start].SetName('')
            temp = self.Node[self.Start].GetPointer()
            self.Node[self.Start].SetPointer(self.NextFree)
            self.NextFree = self.Start
            self.Start = temp
        
                
        else:
            prev = self.Start
            curr = self.Node[prev].GetPointer()
            for i in range(1, position-1):
                prev = curr
                curr = self.Node[curr].GetPointer()
            
            Temp = self.Node[curr].GetPointer()
            self.Node[prev].SetPointer(Temp)
            self.Node[curr].SetName('')
            self.Node[curr].SetPointer(self.NextFree)
            self.NextFree = curr
                    
            
    
    def Length(self):
        if self.Start == 0:
            return 0
        else:
            i = 0
            currNode = self.Node[self.Start]
            while True:
                i += 1
                if currNode.GetPointer() == 0:
                    break
            return i
                
    def IsEmpty(self):
        return self.Start == 0
    
    def IsFull(self):
        return self.NextFree > 10
    
    def display(self):
        print('Start:', self.Start)
        print('NextFree:', self.NextFree)
        print('%-15s %-15s %-15s' % ('Index', 'Name', 'Pointer'))
        for i in range(1, 11):
            node = self.Node[i]
            print('%-15s %-15s %-15s' % (i, node.GetName(), node.GetPointer()))
            
    def traverse(self):
        currNode = self.Node[self.Start]
        while True:
            print(currNode.GetName(), end=',')
            if currNode.GetPointer() == 0:
                break
            currNode = self.Node[currNode.GetPointer()]
    
    

def main():
    lst = LinkedList()
    lst.Insert('Ali', 1)
    lst.Insert('Jack', 1)
    lst.Insert('Ben',2)
    lst.Delete(1)
    lst.Insert('Jane', 2) 
    lst.Insert('Ken', 3)   # Ben, Jane, Ken, Ali
    lst.Delete(2)
    lst.display()
    print()
    lst.traverse()



if __name__ == '__main__':
    main()