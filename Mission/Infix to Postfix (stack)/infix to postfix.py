##infix to postfix

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

def peek(stack):
    return stack[-1]




def infix_to_postfix(string):
    
    number = make_empty_stack()
    operator = make_empty_stack()
    postfix = ''
    
    for ele in string:
        if ele.isdigit():
            push(number, ele)
            
        elif ele == ')':
            while True:
                if peek(operator) == '(':
                    pop(operator)
                    break
                else:
                    push(number, pop(operator))
                    else:
            while True:
                if len(operator) == 0 or peek(operator) in '+-(' or ele == '(':
                    break
                else:
                    push(number, pop(operator))
            push(operator, ele)

    for ele in operator:
        push(number, ele)

    for ele in number:
        postfix += ele
    return postfix





##print(infix_to_postfix('3+4'))
##print(infix_to_postfix('3+4-2'))
##print(infix_to_postfix('3*4-2'))
##print(infix_to_postfix('1+2*3'))
##print(infix_to_postfix('(1+2)*3'))
print(infix_to_postfix('(1+2)*(3+4)'))
print(infix_to_postfix('3*4+5'))
print(infix_to_postfix('3*(4+5)/2'))
