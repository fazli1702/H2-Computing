def print_tree(tree, print_output=True):
    """
    Helper function to print trees in this mission.

    Yes, it looks scary. Nothing to see here (:
    """
    
    def get_elements_at_level(tree, level):
        def helper(tree, level, cur):
            if is_empty_tree(tree) and cur < level:
                dummy = build_tree(" ", make_empty_tree(), make_empty_tree())
                return helper(left_branch(dummy), level, cur + 1) + helper(right_branch(dummy), level, cur + 1)
            if cur == level:
                if is_empty_tree(tree):
                    return (" ", )
                else:
                    return (entry(tree), )
            elif cur < level:
                return helper(left_branch(tree), level, cur + 1) + helper(right_branch(tree), level, cur + 1)
        return helper(tree, level, 0)

    def height(tree):
        if is_empty_tree(tree):
            return 0
        else:
            return 1 + max(height(left_branch(tree)), height(right_branch(tree)))

    h = height(tree)
    output_string = ""

    for level in range(h):
        indent = 2 ** (h - (level + 1)) - 1
        spacing = 2 ** (h - level) - 1

        output = " " * indent

        for i, e in enumerate(get_elements_at_level(tree, level)):
            if level == 0 or i == 0:
                output = output + str(e)
            else:
                output = output + " " * spacing + str(e)
        if print_output:
            print(output)
        else:
            output_string += output + '/'
    if not print_output:
        return output_string





# question 1

###########
# BST Constructor#
###########
def build_tree(entry, left, right):
    return [entry, left, right]

###########
# BST Accessors #
###########
def entry(tree):
    return tree[0]
    
    
def left_branch(tree):
    return tree[1]


def right_branch(tree):
    return tree[2]

###########
# Empty tree constructor #
###########
def make_empty_tree():
    return []

###########
# Predicate #
###########
def is_empty_tree(tree):
    return tree == []






####DO NOT REMOVE/MODIFY###############
tree0= build_tree(10,make_empty_tree(),make_empty_tree())
tree1= build_tree(1,build_tree(2,make_empty_tree(),make_empty_tree()),build_tree(3,make_empty_tree(),make_empty_tree()))
tree2= build_tree(4,build_tree(5,make_empty_tree(),make_empty_tree()),build_tree(6,make_empty_tree(),make_empty_tree()))
tree3=build_tree(7,build_tree(8,make_empty_tree(),make_empty_tree()),build_tree(9,make_empty_tree(),make_empty_tree()))



##print(is_empty_tree(make_empty_tree()))
##print(entry(tree1))
##print(left_branch(tree2))
##print(right_branch(tree3))
##print(left_branch(tree0))
##print(right_branch(tree0))








#question 2
def contains(x, tree):
    if is_empty_tree(tree) == True:
        return False
    elif entry(tree) == x:
        return True
    elif x > entry(tree):
        return contains(x, right_branch(tree))
    elif x < entry(tree):
        return contains(x, left_branch(tree))



t1 = build_tree(2, build_tree(1, make_empty_tree(),make_empty_tree()) ,build_tree(3, make_empty_tree (),make_empty_tree ()))
t2 = build_tree (5, build_tree (2, build_tree (1, make_empty_tree (),make_empty_tree ()) ,make_empty_tree ()) ,build_tree (7, make_empty_tree (),build_tree (10 , make_empty_tree (),make_empty_tree ())))


##print(t1)
##print(t2)
##print(contains(2, t1))
##print(contains(1, t2))
##print(contains(3, t2))













#question 4
def insert_tree(x, tree):
    if is_empty_tree(tree) == True:
        return build_tree(x, make_empty_tree(), make_empty_tree())
    elif x > entry(tree):
        return build_tree(entry(tree), left_branch(tree), insert_tree(x, right_branch(tree)))
    else:
        return build_tree(entry(tree), insert_tree(x, left_branch(tree)), right_branch(tree))
                     
                
                                      
            
t = build_tree(5, make_empty_tree(), make_empty_tree())
##print('t:', t)
##print(insert_tree(7, t))


t1 = build_tree(2, build_tree(1, make_empty_tree(),make_empty_tree()) ,build_tree(3, make_empty_tree (),make_empty_tree ()))
##print('t1:', t1)
t1= insert_tree (5, t1)
##print('t1 new:', t1)
t2 = build_tree (5, build_tree (2, build_tree (1, make_empty_tree (),make_empty_tree ()) ,make_empty_tree ()) ,build_tree (7, make_empty_tree (),build_tree (10 , make_empty_tree (),make_empty_tree ())))
##print('t2:', t2)
t2= insert_tree (6, t2)
##print('t2 new:', t2)



##print(entry(right_branch(right_branch(t1))))
##print(entry(left_branch(right_branch(t2))))


new_tree = make_empty_tree()
for ele in ["June", "April", "January", "May", "February", "September", "October", "December"]:
    insert_tree(ele, new_tree)
print(new_tree)







#question 7
def flatten(tree):
    if is_empty_tree(tree):
        return []
    else:
        return flatten(left_branch(tree)) + [entry(tree)] + flatten(right_branch(tree))

t3= build_tree(5, build_tree(2, build_tree(1, make_empty_tree(), make_empty_tree()), make_empty_tree()), build_tree(7,make_empty_tree(), build_tree(10, make_empty_tree(), make_empty_tree())))
##print(print_tree(t3))
##print(flatten(t3))




#question 8
def flatten_pre(tree):
    if is_empty_tree(tree):
        return []
    else:
        return [entry(tree)] + flatten_pre(left_branch(tree)) + flatten_pre(right_branch(tree))


##print(flatten_pre(t3))



#question 9
def flatten_post(tree):
    if is_empty_tree(tree):
        return []
    else:
        return flatten_post(left_branch(tree)) + flatten_post(right_branch(tree)) + [entry(tree)]

##print(flatten_post(t3))
