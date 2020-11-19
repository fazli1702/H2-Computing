def isOpenBracket(ele):
    return ele in ['(', '[', '{']

def isCloseBracket(ele):
    return ele in [')', ']', '}']

def checkBracket(Open, Close):
    if Open == '(':
        return Close == ')'
    elif Open == '[':
        return Close == ']'
    elif Open == '{':
        return Close == '}'


def isBalanced(expression):
    bracket = []
    for i, ele in enumerate(expression):
        if isOpenBracket(ele):
            bracket.append(ele)

        elif isCloseBracket(ele):
            if len(bracket) == 0:
                return False
            else:
                if not checkBracket(bracket.pop(), ele):
                    return False

        if i == len(expression) - 1:
            return len(bracket) == 0


test = ['([8-1]/(5*7))',
        '[(8-1]/(5*7))',
        '{10*2}+3', 
        '{[((10/2)*3)+20]*7}',
        '[(10+5)/2',
        '9/[2+8])',
        '{[([{12/3}])]}]'
]

'''
test case explanation:
1. ([8-1]/(5*7)) - balanced
2. [(8-1]/(5*7)) - not balanced - wrong pair
3. {10*2}+3 - balanced
4. {[((10/2)*3)+20]*7 - balanced
5. [(10+5)/2 - not balanced - no closing bracket for first bracket '[''
6. 9/[2+8]) - not balanced - last closing bracket ')' don't have a paired opening brakcet
7. {[([{12/3}])]}] - not balanced - last closing bracket don't have a paired opening brakcet
'''

def main():
    global test
    for i, ele in enumerate(test):
        print(f'Test {i}: {ele} {isBalanced(ele)}')
main()
