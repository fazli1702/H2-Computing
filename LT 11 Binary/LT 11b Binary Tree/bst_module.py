#####BST_MODULE#########

##################
# BST Constructor#
##################
def build_tree(entry, left, right):
    return [entry,left,right]


##########################
# Empty tree constructor #
#########################
def make_empty_tree():
    return []


################
# BST Accessors #
#################
def entry(tree):
    return tree[0]
      
def left_branch(tree):
    return tree[1]

def right_branch(tree):
    return tree[2]


###########
# Predicate #
###########
def is_empty_tree(tree):
    return tree==[]

def contains(x, tree):
    if is_empty_tree(tree):
        return False
    if entry(tree)==x:
        return True
    if x<entry(tree):
        return contains(x,left_branch(tree))
    else:
        return contains(x,right_branch(tree))
    
###########
# Modifier #
###########

def insert_tree(x, tree):
    if is_empty_tree(tree):
        return build_tree(x,make_empty_tree(),make_empty_tree())
    if x<entry(tree):
        return build_tree(entry(tree),insert_tree(x, left_branch(tree)),right_branch(tree))   
    else:
        return build_tree(entry(tree),left_branch(tree),insert_tree(x, right_branch(tree)))

def flatten(tree):
    if is_empty_tree(tree):
        return []
    elif is_empty_tree(left_branch(tree)) and is_empty_tree(right_branch(tree)):
        return [entry(tree)]
    return flatten(left_branch(tree))+[entry(tree)]+flatten(right_branch(tree))

def flatten_pre(tree):
    if is_empty_tree(tree):
        return []
    elif is_empty_tree(left_branch(tree)) and is_empty_tree(right_branch(tree)):
        return [entry(tree)]
    return [entry(tree)]+ flatten_pre(left_branch(tree))+flatten_pre(right_branch(tree))

def flatten_post(tree):
    if is_empty_tree(tree):
        return []
    elif is_empty_tree(left_branch(tree)) and is_empty_tree(right_branch(tree)):
        return [entry(tree)]
    return flatten_post(left_branch(tree))+flatten_post(right_branch(tree))+[entry(tree)]


##############
# Print tree #
##############
def print_tree(tree, print_output=True):
    """
    Helper function to print trees.

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


