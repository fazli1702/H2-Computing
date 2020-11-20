class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next





class LinkedList():
    def __init__(self, root = None):
        self.root = root

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node

    def add_end(self, data):
        new_node = Node(data)        
        if self.root == None:
            self.root = new_node

        else:
            this_node = self.root
            while this_node:
                if this_node.get_next() == None:
                    this_node.set_next(new_node)
                    break
                this_node = this_node.get_next()



    def sorted_add(self, data):
        if self.root == None:
            self.root = Node(data)

        elif self.root.get_data() > data:
            self.add(data)

        else:
            this_node = self.root
            while this_node:
                Next = this_node.get_next()
                
                if this_node.get_data() < data:
                    
                    if Next == None:
                        this_node.set_next(Node(data))

                    elif Next.get_data() > data:
                        this_node.set_next(Node(data, Next))

                        
                this_node = this_node.get_next()





    def remove_front(self):
        if self.root.get_next() == None:
            self.root = None
        else:
            self.root = self.root.get_next()


    def remove_end(self):
        if self.root.get_next() == None:
            self.root = None

        else:
            this_node = self.root
            while this_node:
                Next = this_node.get_next()
                if Next.get_next() == None:
                    this_node.set_next(None)
                    break
                this_node = this_node.get_next()


    
    def remove(self, data):
        if self.root == None:
            return False

        #if root == data
        elif self.root.get_data() == data:
            self.remove_front()
            return True

        else:
            prev = self.root
            this_node = self.root
            i = 0 
            while this_node:
                Next = this_node.get_next()
                
                if i > 1:
                    prev = prev.get_next()

                #if this_node is last node
                if this_node.get_data() == data:
                    if this_node.get_next() == None:
                        self.remove_end()
                        return True

                    else:
                        prev.set_next(Next)
                        return True
                    
                #print('i:', i)
                #print('prev node:', prev.get_data())
                #print('this node:', this_node.get_data())
                #print('next node:', Next.get_data())
                #print()
                #print()

                
                i += 1
                this_node = this_node.get_next()

                
                
            return False
                
   


    def count(self):
        if self.root == None:
            return 0

        else:
            count = 0
            this_node = self.root
            while this_node:
                count += 1
                this_node = this_node.get_next()
            return count

        

    def print_list(self):
        if self.root == None:
            print('This list has no nodes')

        else:
            this_node = self.root
            while this_node:
                print(this_node.get_data())
                this_node = this_node.get_next()


    def browse(self):
        if self.root == None:
            return []

        else:
            this_node = self.root
            lst = []
            while this_node:
                lst.append(this_node.get_data())
                this_node = this_node.get_next()
            return lst


    def find(self, data):
        if self.root == None:
            return False

        else:
            this_node = self.root
            while this_node:
                if this_node.get_data() == data:
                    return True
                this_node = this_node.get_next()
            return False
        


#q1
        
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(22)

print(myList.print_list())
print(myList.browse())
print(myList.count())
print(myList.find(8))
print(myList.find(7))


#q2
##myList = LinkedList()
##myList.add_end(5)
##myList.add_end(8)
##myList.add_end(22)
##
##myList.print_list()
##print(myList.count())
##print(myList.browse())


#q3
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(22)
myList.add_end(10)
myList.add_end(50)
myList.add_end(7)
##
print(myList.browse())
print(myList.remove_front())
print(myList.browse())
print(myList.remove_end())
print(myList.browse())



#tutorial q1
##myList = LinkedList()
##myList.sorted_add(15)
##myList.sorted_add(8)
##myList.sorted_add(12)
##myList.sorted_add(5)
##myList.sorted_add(18)
##myList.sorted_add(22)
##
##print(myList.browse())



#tutorial q2
myList = LinkedList()
myList.sorted_add(15)
myList.sorted_add(8)
##myList.sorted_add(12)
##myList.sorted_add(5)
##myList.sorted_add(18)
##myList.sorted_add(22)



