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
