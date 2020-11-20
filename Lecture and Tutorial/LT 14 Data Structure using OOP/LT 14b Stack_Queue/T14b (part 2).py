# q1
# Task 4.3 & 4.4

class Queue:
    def __init__(self):
        self.container = []

    def enqueue(self, new):
        if self.isFull():
            return 'Printer is full. New job cannot be added'
        else:
            self.container.append(new)
            return 'Print job added'

    def dequeue(self):
        if len(self.container) == 0:
            return None
        else:
            return self.container.pop(0)

    def isFull(self):
        return len(self.container) == 5

    def output(self):
        print(self.container)




def main():
    Room16 = Queue()
    while True:
        print('-------------------------------------')
        print('1. New print job added to print queue')
        print('2. Next print job output from printer')
        print('3. Current print queue display')
        print()
        print('4. End')
        print('-------------------------------------')

        choice = input('Enter your choice: ')

        if choice == '1':
            job = input('New print job: ')
            Room16.enqueue(job)
            print(job, 'added')

        elif choice == '2':
            print(Room16.dequeue(), 'removed')

        elif choice == '3':
            print(Room16.container)

        elif choice == '4':
            break


main()




#task 4.5, 4.6, 4.7
##Room16 = Queue()
##print(Room16.output())


