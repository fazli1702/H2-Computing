from runes import*

def egyptian(pic, n):
    
    result_left_right = pic
    
    for i in range(n-2):
        result_left_right = stack_frac(1/(i+1), pic, result_left_right)
        result_top_down = pic

    for i in range(n):
         result_top_down = stack_frac(1/(i+1), quarter_turn_left(pic), result_top_down)
         mid_row = stack_frac(1/n, quarter_turn_left(result_left_right), stack_frac((n-2)/(n-1), quarter_turn_left(pic), quarter_turn_left(result_left_right)))
         complete = stack_frac(1/n, quarter_turn_right(result_top_down), stack_frac((n-2)/(n-1), quarter_turn_right(mid_row), quarter_turn_right(result_top_down)))

    return complete

show(egyptian(nova_bb, 9))
