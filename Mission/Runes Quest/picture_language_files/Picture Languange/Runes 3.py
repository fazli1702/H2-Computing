from runes import*

#question 1
def big_small(pic):
    return stack_frac(1/2, quarter_turn_right(quarter_turn_left(quarter_turn_right(nova_bb))), turn_upside_down(pic))

show(big_small(nova_bb))
##show(turn_upside_down(nova_bb))
##show(quarter_turn_right(quarter_turn_left(quarter_turn_right(nova_bb))))
