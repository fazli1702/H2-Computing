### Question 5


####Constructor#####

def make_queue():
    return []            

####Modifier######
def enqueue(q, item):
    q.append(item)

def dequeue(q):
    if q==[]:
        return None
    return q.pop(0)

####Accessors####
def front(q):
    if q==[]:
        return None
    return q[0]

def size(q):
    return len(q)

#######################


### Task 5.1 : Write the program code
###            for delete(q,item) and shift(q,item)

def delete(q, item):
    for i in range(len(q)):
        if q[i] == item:
            q.pop(i)

def shift(q, item):
    for i in range(len(q)):
        if q[i] == item:
            enqueue(q, q.pop(i))





    
