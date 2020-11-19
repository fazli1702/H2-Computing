import csv
from random import *

def lucky_draw():
    f = open('class_s15.csv')
    g = open('class_s16.csv')
    s15 = csv.reader(f)
    s16 = csv.reader(g)

    S15 = []
    c_s15 = []
    
    S16 = []
    c_s16 = []

    S15_S16 = []
    c_s15_s16 = []
    
    for ele in s15:
        S15.append(ele[0])
        c_s15.append(ele[0])
        S15_S16.append(ele[0])
        c_s15_s16.append(ele[0])
        
    for ele in s16:
        S16.append(ele[0])
        c_s16.append(ele[0])
        S15_S16.append(ele[0])
        c_s15_s16.append(ele[0])

    
    ls15 = len(S15)
    a = ls15
    
    ls16 = len(S16)
    b = ls16

    ls15_s16 = len(S15_S16)
    c = ls15_s16
    
    while True:
        print()
        print('1. S15')
        print('2. S16')
        print('3. S15 & S16')
        print()
        print('X. Quit')

        choice = input('Choice:')

        if choice.upper() == 'X':
            
            print('Thank You!')
            return None

##################################################################
#S15


        elif choice == '1':
            while True:
                print('Press any key for name')
                print()

                choice1 = input()

                if choice1.upper() == 'X':
                    return None

                else:
                    if a == 0:
                        print('Reuse names?')
                        print()
                        print('1. Yes')
                        print('2. No')

                        choice2 = input('Choice:')

                        if choice2 != '1':
                            return None
                        else:
                            c_s15 = S15
                            a = ls15
                            #print(a)
                            continue

                    
                    no = randint(0, a-1)
                    print()
                    print(c_s15[no])
                    print()
                    c_s15.pop(no)
                    #print(c_s15)
                    #print(S15)
                    a -= 1



##################################################################
#S16
                    

        elif choice == '2':
            while True:
                print('Press any key for name')
                print()

                choice3 = input()

                if choice3.upper() == 'X':
                    return None

                else:
                    if b == 0:
                        print('Reuse names?')
                        print()
                        print('1. Yes')
                        print('2. No')

                        choice4 = input('Choice:')

                        if choice4 != '1':
                            return None
                        else:
                            c_s16 = S16
                            b = ls16
                            #print(b)
                            continue

                    
                    no = randint(0, b-1)
                    print()
                    print(c_s16[no])
                    print()
                    c_s16.pop(no)
                    #print(c_s16)
                    #print(S16)
                    b -= 1

                    
#########################################################################
#S15 & S16


        elif choice == '3':
            while True:
                print('Press any key for name')
                print()

                choice5 = input()

                if choice5.upper() == 'X':
                    return None

                else:
                    if c == 0:
                        print('Reuse names?')
                        print()
                        print('1. Yes')
                        print('2. No')

                        choice6 = input('Choice:')

                        if choice6 != '1':
                            return None
                        else:
                            c_s15_s16 = S15_S16
                            c = ls15_s16
                            #print(b)
                            continue

                    
                    no = randint(0, c-1)
                    print()
                    print(c_s15_s16[no])
                    print()
                    c_s15_s16.pop(no)
                    #print(c_s16)
                    #print(S16)
                    c -= 1
            





#########################################################################

        else:
            print('Invalid choice')
            
        


lucky_draw()
