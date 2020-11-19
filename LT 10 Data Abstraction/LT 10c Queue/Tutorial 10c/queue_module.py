#####Queue ADT####
#####Queue module#####

####Constructor#####
def make_empty_queue():
    return []

def make_queue(seq):
    return list(seq)

###predicates
def is_empty_queue(q):
    return q==[]

####Modifier######
def enqueue(q, item):
    q.append(item)

def dequeue(q):
    if is_empty_queue(q):
        return None
    return q.pop(0)

def clear(q):
    q.clear()

####Accessors####
def front(q):
    if q==[]:
        return None
    return q[0]
    
def size(q):
    return len(q)

###print q
def show_q(q):
    print('H <', q, '> T') 
    
