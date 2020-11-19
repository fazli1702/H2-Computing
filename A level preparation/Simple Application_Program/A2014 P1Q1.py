# task 1.1
def main():
    with open('JARGON.txt', 'r') as f:
        data = f.readlines()
        terms = [row.strip() for row in data]

    header = '+' * 20
    while True:
        print(header)
        print('1. Exact Match')
        print('2. Start of word')
        print('3. Within word')
        print(header)

        choice = int(input('Choice?'))
        word = input('word?')

        if word == 'XXX':
            break

        if choice == 1:
            counter = 0
            for ele in terms:
                if ele == word:
                    print(ele)
                    counter += 1
            print(f'There were {counter} matching item(s) \n')


        if choice == 2:
            i = len(word)
            counter = 1
            for ele in terms:
                if ele[:i] == word:
                    print(ele)
                    counter += 1
            print(f'There were {counter} matching item(s) \n')


        if choice == 3:
            counter = 0
            for ele in terms:
                if word in ele:
                    print(ele)
                    counter += 1
            print(f'There were {counter} matching item(s) \n')


# task 1.2
## create own test case
test1 = 'design'    # exact match
test2 = 'box'       # within word
test3 = 'sys'       # start of word
test4 = 'hello'     # errornoues

main()

        
