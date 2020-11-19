class DataStructure:
    def __init__(self, seq=[]):
        self.container = []
        for value in seq:
            self.container.append(value)

    def add(self, value):
        self.container.append(value)

    def is_empty(self):
        return len(self.container) == 0

    def output(self):
        if len(self.container) == 0:
            print('Empty DataStructure')
        else:
            s = ''
            for value in self.container:
                s += ' < ' + str(value)
            print(s)



class Stack(DataStructure):
    def __init__(self, seq=[]):
        super().__init__(seq)

    def push(self, value):
        super().add(value)

    def pop(self):
        if len(self.container) == 0:
            return False
        else:
            return self.container.pop()

    def output(self):
        if len(self.container) == 0:
            print('Empty Stack')

        else:
            s = ''
            print('< < < STACK < < <')
            for value in self.container:
                s += ' < ' + str(value)
            print(s)



class Queue(DataStructure):
    def __init__(self, seq=[]):
        super().__init__(seq)

    def enqueue(self, value):
        super().add(value)

    def dequeue(self):
        if len(self.container) == 0:
            return False
        else:
            return self.container.pop(0)

    def output(self):
        if len(self.container) == 0:
            print('Empty Queue')
        else:
            s = ''
            print('< < < QUEUE < < <')
            for value in self.container:
                s += ' < ' + str(value)
            print(s)




s = Queue()
s.enqueue(5)
s.enqueue(8)
s.enqueue(22)
s.output()



