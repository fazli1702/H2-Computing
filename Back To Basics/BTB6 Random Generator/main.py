import random
import csv

def class_S15():
    student = []
    with open('19S15.txt') as file:
        reader = csv.reader(file)
        for row in reader:
            student += row
    return student


def class_S16():
    student = []
    with open('19S16.txt') as file:
        reader = csv.reader(file)
        for row in reader:
            student += row
    return student


def main():
    S15 = class_S15()
    S16 = class_S16()

    while True:
        if len(S15) == 0:
            print('All students from S15 have been chosen')
            print('Please chooe your next action')
            print()
            print('1. Choose from class again')
            print('2. Quit')

            choice = int(input('Please enter your choice:'))
            
            if choice == 1:
                S15 = class_S15()
                
            elif choice == 2:
                break
        
        elif len(S16) == 0:
            print('All students from S16 have been chosen')
            print('Please chooe your next action')
            print()
            print('1. Choose from class again')
            print('2. Quit')

            choice = int(input('Please enter your choice:'))
            
            if choice == 1:
                S16 = class_S16()
                
            elif choice == 2:
                break

        
        print('------ MENU ------')
        print()
        print('1. 19S15')
        print('2. 19S16')
        print()
        print('3. Quit')

        choice = int(input('Please enter your choice:'))

        if choice == 1:
            i = random.randint(0, len(S15)-1)
            print()
            print(S15.pop(i))
            print()
            
        elif choice == 2:
            i = random.randint(0, len(S16)-1)
            print()
            print(S16.pop(i))
            print()

        elif choice == 3:
            break

        else:
            print('Please enter the correct choice')


main()
