class Stack():
    def __init__(self, seq = []):
        self.container  = []
        for value in seq:
            self.container.append(value)
        
    def push(self, value):
        print('add value: {}'.format(value))
        self.container.append(value)

    def pop(self):
        if len(self.container) == 0:
            return False
        else:
            return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def output(self):
        if len(self.container) == 0:
            print('Empty Stack')
        else:
            s = ' '
            print('< < < STACK < < <')
            for ele in self.container:
                s = s + ' < ' + str(ele)
            print(s)


##s = Stack()
##s.push(5)
##s.push(8)
##s.push(22)
##s.output()



class Queue():
    def __init__(self, seq=[]):
        self.container = []
        for value in seq:
            self.container.append(value)

    def enqueue(self, value):
        print('add value: {}'.format(value))
        self.container.append(value)

    def dequeue(self):
        if len(self.container) == 0:
            return False
        else:
            return self.container.pop(0)

    def is_empty(self):
        return len(self.container) == 0

    def output(self):
        if self.is_empty():
            print('Empty Queue')
        else:
            s = ''
            print('< < < QUEUE < < <')
            for value in self.container:
                s += ' < ' + str(value)
            print(s)



q = Queue()
q.enqueue(5)
q.enqueue(8)
q.enqueue(22)
q.output()

        
