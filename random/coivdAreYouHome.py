def are_you_home():
    print('ARE YOU HOME?')
    print()
    print('1. True')
    print('2. False')
    ans = input('1/2: ')
    
    if ans == '1':
        print('GOOD JOB STAY THERE!')

    else:
        print('GO HOME!')
        while True:
            print('ARE YOU HOME NOW?')
            print()
            print('1. True')
            print('2. False')

            ans2 = input('1/2: ')

            if ans2 == '1':
                print('GOOD JOB STAY THERE')
                break

are_you_home()
                            
