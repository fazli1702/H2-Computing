# TASK 3.1
from random import randint

def LicenceKey():
    character = 'abcdefghijklmnopqrstuvwxyz'
    key = ''
    for i in range(9):
        j = randint(0, len(character)-1)
        key += character[j].upper()

    multiplier = 1
    total = 0
    for ele in key:
        product = ord(ele) * multiplier
        total += product
        multiplier += 1

    checkDigit = total % 11
    if checkDigit == 10:
        return key + 'X'
    else:
        return key + str(checkDigit)





def displayFile():
    with open('LICENCE-KEYS.TXT') as f:
        data = f.readlines()
        for ele in data:
            print(ele.strip())

def appendFile(key):
    with open('LICENCE-KEYS.TXT', 'a') as f:
        f.write(key)
        

# TASK 3.2
def main():
    while True:
        print('1. Purchase of a new licence for either single-uesr or 3-user licence')
        print('2. Register an additional user to an active 3-user licence')
        print('3. End')

        choice = input('Please enter your choice:')

        # TASK 3.3
        if choice == '1':
            print('Type of licence')
            print('1. Single-user')
            print('2. 3-user')

            choice2 = input('Enter your choice:')

            if choice2 == '1':
                key = LicenceKey() + ' 1'

            elif choice2 == '2':
                key = LicenceKey() + ' 3 1'

            # print(key)
            appendFile(key+'\n')
            displayFile()


        # TASK 3.4
        elif choice == '2':
            update = False
            with open('LICENCE-KEYS.TXT') as f:
                data = f.readlines()
                for row in data:
                    row = row.strip().split()
                    if len(row) == 3:
                        # print(row)
                        if row[2] != '3':
                            new = str(int(row[2]) + 1)
                            row[2] = new
                            update = True
                            
                if not update:
                    print('All active users are full')
                        

        elif choice == '3':
            break
        else:
            print('Please enter 1/2/3')







# TASK 3.5
class Licence:
    def __init__(self, key, licenceType, purchaseDate, name, MAC):
        self.key = key
        self.licenceType = licenceType
        self.purchaseDate = purchaseDate
        self.name = name
        self.MAC = MAC

    def setName(self, new):
        self.name = new


class SingleUserRegistration(Licence):
    def __init__(self):
        super().__init__()


class 3UserRegistration(Licence):
    def __init__(self):
        super().__init__()

    def setName(self, new):
        if len(self.name) == 1:
            self.name = [self.name, new]
        elif len(self.name) == 3:
            print('No more availble user')
        else:
            self.name.append(new)

