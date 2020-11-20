class Node:
    def __init__(self, data):
        self.data = data
        self.leftptr = -1
        self.rightptr = -1

    def get_data(self):
        return self.data
    
    def get_leftptr(self):
        return self.leftptr

    def get_rightptr(self):
        return self.rightptr

    def set_data(self, new_data):
        self.data = new_data
        
    def set_leftptr(self, new_leftptr):
        self.leftptr = new_leftptr

    def set_rightptr(self, new_rightptr):
        self.rightptr = new_rightptr

    def display(self):
        print('data:', data)
        print('leftptr:', leftptr)
        print('rightptr:', rightptr)


n1=Node(5)
n2=Node(9)
n3=Node(13)
d1=n1.get_data()
n2.set_leftptr(2)
l2=n2.get_leftptr()
n3.set_rightptr(3)
r3=n3.get_rightptr()
n2.set_data(8)
d2=n2.get_data()


    
# print(d1)
# print(l2)
# print(r3)
# print(d2)





class Tree:
    def __init__(self):
        self.root = -1
        self.tree = []
        self.next_position = 0


    def add(self, value):
        new_node = Node(value)
        self.tree.append(new_node)

        if self.root == -1:
            self.root = 0
            
        else:
            if self.next_position % 2 == 1:
                k = (self.next_position - 1) // 2
                self.tree[k].set_leftptr(self.next_position)

            else:
                k = (self.next_position - 2) // 2
                self.tree[k].set_rightptr(self.next_position)
                
        self.next_position += 1



    def inorder(self, curr_i = 0):
        #Left, Node, Right
        if self.root == -1:
            return 'Empty Tree'

        current = self.tree[curr_i]

        #check if leaf node
        if current.get_leftptr() == -1 and current.get_rightptr() == -1:
            print(current.get_data())

        else:
            #traverse left sub tree
            if current.get_leftptr() != -1:
                curr_i = current.get_leftptr()
                self.inorder(curr_i)

            #node
            print(current.get_data())

            #traverse right sub tree
            if current.get_rightptr() != -1:
                curr_i = current.get_rightptr()
                self.inorder(curr_i)


        

    def display(self):
        print('root:', self.root)
        lst = []
        for i in range(len(self.tree)):
            print('index:', i, '\tdata:', self.tree[i].get_data(),
                  '\tleftptr:', self.tree[i].get_leftptr(), '\trightptr:',
                  self.tree[i].get_rightptr())
            lst.append(self.tree[i].get_data())
        print(lst)
        


t1 =Tree()
t1.add('A')
t1.add('B')
t1.add('C')
t1.add('D')
t1.add('E')
t1.add('F')
t1.add('G')
##print(t1.display())
##print(t1.inorder())
		
