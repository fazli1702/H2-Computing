'''
task 4.1

Test Number | User ID    | Return Value | Explanation of test case
     1      | 2015_0987  |      0       | Valid User ID   
     2      | 2015_12345 |      1       | Length of User ID more than 9 (10)
     3      | 2010_0987  |      2       | First 4 digits are not 2015 (2010)
     4      | 2015_BA87  |      3       | Last 4 characters are not digits (BA87)
'''


# task 4.2
def ValidateUserID(ThisUserID:str) -> int:
    if len(ThisUserID) > 9:
        return 1
    elif len(ThisUserID) == 9:
        if ThisUserID[:4] != '2015':
            return 2
        elif not ThisUserID[5:].isnumeric():
            return 3
        else:
            return 0

def main():
    test = ['2015_0987', '2015_12345', '2010_0987', '2015_BA87']
    for ele in test:
        print(ValidateUserID(ele))




# task 4.3
class PrintJob:
    def __init__(self, userID, terminal, size):
        self.userID = userID
        self.terminal = terminal
        self.size = size

    def getUserID(self):
        return self.userID

    def getTerminal(self):
        return self.terminal

    def getSize(self):
        return self.terminal


class Queue:
    def __init__(self, name):
        self.name = name
        self.lst = []

    def push(self, newJob):
        if len(self.lst) == 5:
            print('Print queue is full')
        else:
            self.lst.append(newJob)

    def pop(self):
        job = self.lst.pop(0)
        print(job.getUserID(), job.getTerminal(), job.getSize())

    def display(self):
        print('%-10s %-10s %-10s' % ('userID', 'terminal', 'size'))
        for job in self.lst:
            print('%-10s %-10s %-10s' % (job.getUserID(), job.getTerminal(), job.getSize()))




def main2():
    Room16 = Queue('Room16')
    while True:
        print('1. New print job added to print queue')
        print('2. Next print job output from printer')
        print('3. Current print queue displayed')
        print('4. End')

        choice = int(input('Enter your choice:'))

        if choice == 1:
            # userID = input('Enter userID:')
            # terminal = int(input('Enter terminal:'))
            # size = int(input('Enter size of file:'))
            # job = PrintJob(userID, terminal, size)
            job = PrintJob('2015_0987', 120, 200)
            job2 = PrintJob('2015_0986', 100, 177)
            job3 = PrintJob('2015_0985', 97, 596)
            Room16.push(job)
            Room16.push(job2)
            Room16.push(job3)

        elif choice == 2:
            Room16.pop()

        elif choice == 3:
            Room16.display()

        elif choice == 4:
            break

main2()