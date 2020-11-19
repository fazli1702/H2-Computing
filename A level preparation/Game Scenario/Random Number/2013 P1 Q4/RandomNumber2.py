def main():
    # input
    distribution = {}
    while True:
        x = input('Next X value ... <ZZZ to END> ')
        if x.upper() == 'ZZZ':
            break

        n = int(input('Frequency ... '))
        distribution[x] = n


    # display
    print('\n\n')
    print('+'*20)
    print('Frequency distribution')
    print('+'*20)
    print()

    for key, value in distribution.items():
        print('%-15s %-15s' % (key, '@'*value))


    


