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
