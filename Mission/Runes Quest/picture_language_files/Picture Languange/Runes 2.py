from runes import*

##show(stack_frac(1/3,heart_bb, stack(heart_bb, heart_bb)))
##show(stack_frac(1/3,heart_bb, stack_frac(1/2,heart_bb, heart_bb)))
##show(stack(stack_frac(1/3,heart_bb,heart_bb), heart_bb))
##show(stack(stack(heart_bb,heart_bb), heart_bb))
##show(stack_frac(2/3, stack(heart_bb, heart_bb), heart_bb))
##show(stack_frac(2/3, stack_frac(1/2, heart_bb, heart_bb), heart_bb))






#question 3
def evenly_beside(rune):
    result = rune
    for n in range(5):
        result = stack_frac(1/(n+1), quarter_turn_left(rune), result)
    return (quarter_turn_right(result))



show(evenly_beside(nova_bb))


    
