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
        for ele in seq:
            #empty linked list
            if self.NextFree == 1:
                self.Table[1].setDataValue(ele)
                self.Table[1].setPointer(0)
                self.NextFree += 1

            else:
                self.Table[self.NextFree].setDataValue(ele)
                self.Table[self.NextFree].setPointer(0)
                self.Table[self.NextFree - 1].setPointer(self.NextFree)
                self.NextFree += 1


    def Count(self, string):
        #traverse linked list
        for i in range(1, 27):
            current = self.Table[i]

            if current.getDataValue() == '':
                break
            
            count = 0
            for ele in string:
                if ele == current.getDataValue():
                    count += 1
                current.setCounter(count)




    def display(self):
        print('%-15s %-15s %-15s %-15s' % ('Index', 'Data', 'Counter', 'Pointer'))
        for i in range(1, 27):
            print('%-15s %-15s %-15s %-15s' % (i, self.Table[i].getDataValue(), self.Table[i].getCounter(), self.Table[i].getPointer()))



def main():
    f = open('Our+Song.txt')
    lst = LinkedList()
    lst.Add('AEIOU')
    lines = f.readlines()
    string = ''
    for line in lines:
        string += str(line)
    lst.Count(string)
    lst.display()

##main()






###############################################


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
        if self.content == []:
            return None

        else:
            output = None
            for i in range(len(self.content)):
                if self.content[0] == title:
                    output = self.dequeue()
                else:
                    self.enqueue(self.dequeue())

            return output
        


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
Popular2019.display()
print()
a = Popular2019.delete("Bad Guy")
b = Popular2019.delete("Our College Song")          
Popular2019.display()
