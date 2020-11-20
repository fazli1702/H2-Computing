def make_stack(seq):
    new_stack=[]
    for element in seq:
        new_stack.append(element)
    return new_stack

def make_empty_stack():
    return []

def is_empty_stack(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    return None

def pop(stack):
    if len(stack)==0:
        return None
    else:
        return stack.pop()

def peek(stack):
    if len(stack)==0:
        return None
    else:
        return stack[-1]
    
def clear(stack):
    return stack.clear()

def show(stack):
    print('<TOP')
    for i in stack[::-1]:
        print(i)
    print('<BOTTOM')
    return None

def size(stack):
    return len(stack)


    
