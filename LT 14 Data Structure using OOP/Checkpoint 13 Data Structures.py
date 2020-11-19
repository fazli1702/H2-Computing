class Node:
    def __init__(self):
        self.DataValue = ''
        self.Counter = 0
        self.Pointer = 0


    def getDataValue(self):
        return self.DataValue

    def getCounter(self):
        return self.Counter

    def getPointer(self):
        return self.Pointer

    def setDataValue(self, new):
        self.DataValue = new

    def setCounter(self, new):
        self.Counter = new

    def setPointer(self, new):
        self.Pointer = new


class LinkedList:
    def __init__(self):
        self.Table = [Node() for i in range(27)]
        self.Start = 1
        self.NextFree = 1

        for i in range(1, 26):
            self.Table[i].setPointer(i+1)

    def Add(self, seq):
        for value in seq:
            #empty linked list
            if self.NextFree == 1:
                self.Table[self.NextFree].setDataValue(value)
                self.Table[self.NextFree].setPointer(0)
                self.NextFree += 1

            else:
                self.Table[self.NextFree-1].setPointer(self.NextFree)
                self.Table[self.NextFree].setDataValue(value)
                self.Table[self.NextFree].setPointer(0)
                self.NextFree += 1


    def Count(self, string):
        #empty bst
        if self.NextFree == 1:
            return 0

        else:
            #traverse linked list
            for i in range(1, 27):
                curr = self.Table[i]
                
                #if empty node, break
                if curr.getDataValue == '':
                    break
                
                count = 0
                for ele in string:
                    if ele == curr.getDataValue():
                        count += 1
                        
                curr.setCounter(count)
                

                


    def display(self):
        print('start:', self.Start)
        print('next free:', self.NextFree)
        print('%-15s %-15s %-15s %-15s' % ('Index', 'DataValue', 'Counter', 'Pointer'))
        for i in range(1, len(self.Table)):
            print('%-15s %-15s %-15s %-15s' % (i, self.Table[i].getDataValue(),
                                               self.Table[i].getCounter(),
                                               self.Table[i].getPointer()))


lst = LinkedList()
lst.Add('AEIOU')
lst.Count('YISHUN INNOVA JUNIOR COLLEGE')
##lst.Add('ABC')
##lst.Count( '12A3ACDAEF')
lst.display()




class Queue():
    def __init__(self):
        self.content = []

    def enqueue(self,item):
        self.content.append(item)

    def dequeue(self):
        if len(self.content)>0:
            return self.content.pop(0)
        else:
            return None

    def display(self):
        if len(self.content) == 0:
            print('Queue is empty')
        else:
            for i in range (len(self.content)):
                print(i+1, self.content[i])
                

# Write the code for class PlayList below here:

class PlayList(Queue):
    def __init__(self):
        super().__init__()

    def delete(self, title):
        #empty q
        if len(self.content) == 0:
            return None

        #remove front of queue
        elif self.content[0] == title:
            return self.dequeue()

        else:
            lst = Queue()
            delq = Queue()   #for outputing data later
            while len(self.content) != 0:
                if self.content[0] == title:
                    delq.enqueue(self.dequeue())
                else:
                    lst.enqueue(self.dequeue())

            for ele in lst.content:
                self.enqueue(ele)

            return delq.dequeue()
                




# Do not remove the following:
Popular2019 = PlayList()
Popular2019.enqueue("Motivation")
Popular2019.enqueue("Boyfriend")
Popular2019.enqueue("Love Like That")
Popular2019.enqueue("Looking For America")
Popular2019.enqueue("La Canción")
Popular2019.enqueue("Borderline")
Popular2019.enqueue("Bad Guy")
Popular2019.enqueue("Simmer")
##Popular2019.display()

##print('----------')

a = Popular2019.delete("Bad Guy")
b = Popular2019.delete("Our College Song")
c = Popular2019.delete("Motivation")
##Popular2019.display()

##print('----------')
##
##print(a)
##print(b)
##print(c)   
                








