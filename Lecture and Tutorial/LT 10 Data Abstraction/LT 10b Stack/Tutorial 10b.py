#question 1
def make_empty_stack():
    return []

def push(stack, item):
    if type(item) == str:
        stack += list(item)
    elif type(item) == int or type(item) == float:
        stack += [item]

def pop(stack):
    if stack == []:
        return None
    else:
        return stack.pop()

def reverse(string):
    s = make_empty_stack()
    reverse = ''
    for ele in string:
        push(s, ele)

    for i in range(len(string)):
        reverse += pop(s)

    return reverse

##print(reverse('sentosa'))
##print(reverse('noel sees leon'))






#question 2
def check_bracket(string):
    s = make_empty_stack()

    for ele in string:
        if ele == '(':
            push(s, ele)
        elif ele == ')':
            if len(s) == 0:
                return False
            else:
                pop(s)

    if len(s) == 0:
        return True
    else:
        return False



            
##print(check_bracket('((()))'))
##print(check_bracket('(()))'))











#question 3
def calculate(inputs):
    s = make_empty_stack()
    for ele in inputs:
        if ele == '+':
            a = pop(s)
            b = pop(s)
            c = b + a
            push(s, c)
        elif ele == '-':
            a = pop(s)
            b = pop(s)
            c = b - a
            push(s, c)
        elif ele == '*':
            a = pop(s)
            b = pop(s)
            c = b * a
            push(s, c)
        elif ele == '/':
            a = pop(s)
            b = pop(s)
            c = b / a
            push(s, c)
        else:
            push(s, ele)
    return pop(s)



##print(calculate((1, 2, '+', 3, '*')))
##print(calculate((1, 2, '+')))
##print(calculate((1, 25, '+', 3, '*')))
##print(calculate((3, 1, 2, '+', '*')))
##print(calculate((28, )))
##print(calculate((1, 2, '+', 3, '/')))
##print(calculate((5, 2, '/', 4, '*')))
##print(calculate((1, 2, '*', 3, '-', 2, '*', 5, '+')))
##print(calculate((5, 1, 20, 2, '+', 23, 12, '-', '/', '+', '*')))
            
