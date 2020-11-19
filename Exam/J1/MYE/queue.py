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









