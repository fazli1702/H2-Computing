from Tutorial_11b import *

#question 1
def predecessor(x, tree):
    in_order = flatten(tree)
    for i in range(len(in_order)):
        if in_order[i] == x:
            if i == 0:
                return None
            else:
                return in_order[i-1]
    return None


t3= build_tree(5, build_tree(2, build_tree(1, make_empty_tree(), make_empty_tree()), make_empty_tree()), build_tree(7,make_empty_tree(), build_tree(10, make_empty_tree(), make_empty_tree())))


##print(predecessor(5, t3))
##print(predecessor(10, t3))
##print(predecessor(1, t3))





#question 2
def successor(x, tree):
    in_order = flatten(tree)
    for i in range(len(in_order)):
        if in_order[i] == x:
            if i == len(in_order)-1:
                return None
            else:
                return in_order[i+1]
    return None



##print(successor(1, t3))
##print(successor(10, t3))
##print(successor(7, t3))
##print(successor(2, t3))






#question 3
def is_leaf(x, tree):
    x_tree = build_tree(x, make_empty_tree(), make_empty_tree())
    
    if x == entry(tree):
        if x_tree == tree:
            return True
        return False

    elif x > entry(tree):
        return is_leaf(x, right_brancH(tree))

    else:
        return is_leaf(x, left_branch(tree))


##print(is_leaf(2,t3))
##print(is_leaf(1,t3))
##print(is_leaf(5,t3))






#question 4
def has_one_child(x, tree):
    if x == entry(tree):
        if is_empty_tree(left_branch(tree)) == True and is_empty_tree(right_branch(tree)) == False:
            return True
        elif is_empty_tree(left_branch(tree)) == False and is_empty_tree(right_branch(tree)) == True:
            return True
        return False

    elif x > entry(tree):
        return has_one_child(x, right_branch(tree))

    else:
        return has_one_child(x, left_branch(tree))



##print(has_one_child(5,t3))
##print(has_one_child(2,t3))
##print(has_one_child(1,t3))







#question 5
def delete_tree_p(x, tree):
    
    if is_leaf(x, tree):
        x_tree = build_tree(x, make_empty_tree(), make_empty_tree())
        if tree == x_tree:
            return make_empty_tree()
        elif x > entry(tree):
            return build_tree(entry(tree), left_branch(tree) ,delete_tree_p(x, right_branch(tree)))
        else:
            return build_tree(entry(tree), delete_tree_p(x, left_branch(tree)), right_branch(tree))
        
    elif has_one_child(x, tree):
        if entry(tree) == x:
            if is_empty_tree(right_branch(tree)):
                return left_branch(tree)
            else:
                return right_branch(tree)
        elif x > entry(tree):
            return build_tree(entry(tree), left_branch(tree) ,delete_tree_p(x, right_branch(tree)))
        else:
            return build_tree(entry(tree), delete_tree_p(x, left_branch(tree)), right_branch(tree))
        
    else:
        if entry(tree) == x:
            return build_tree(entry(left_branch(tree)), left_branch(left_branch(tree)), right_branch(tree))

    
        


##print('t3:', t3)
##print(print_tree(t3))
##print('t3 delete 1:', delete_tree_p(1,t3))
##print(print_tree(delete_tree_p(1,t3)))
##print('t3 delete 2:', delete_tree_p(2, t3))
##print(print_tree(delete_tree_p(2, t3)))
##print('t3 delete 5:', delete_tree_p(5, t3))
##print(print_tree(delete_tree_p(5, t3)))








#question 6
def delete_tree_s(x,tree):
    if entry(tree) == x:
        
        if is_leaf(x,tree):
            return []
        
        elif has_one_child(x,tree):
            if is_empty_tree(left_branch(tree)):
                if not is_empty_tree(right_branch(tree)):
                    return right_branch(tree)
                
            if is_empty_tree(right_branch(tree)):
                if not is_empty_tree(left_branch(tree)):
                    return left_branch(tree)
                
        else:
            return [successor(x,tree),left_branch(tree),right_branch(right_branch(tree))]
        
    elif entry(tree) >= x:
        return [entry(tree),delete_tree_s(x,left_branch(tree)),right_branch(tree)]
    
    elif entry(tree) <= x:
        return [entry(tree),left_branch(tree),delete_tree_s(x,right_branch(tree))]


    
##print(delete_tree_s(1, t3))
##print(delete_tree_s(1, t3)==[5, [2, [], []], [7, [], [10, [], []]]])
##print(delete_tree_s(5, t3))
##print(delete_tree_s(5, t3)==[7, [2, [1, [], []], []], [10, [], []]])
##print(delete_tree_s(2, t3))
##print(delete_tree_s(2, t3)==[5, [1, [], []], [7, [], [10, [], []]]])
        
