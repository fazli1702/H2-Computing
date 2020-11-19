from runes import*

#question 3
def turn_upside_down(rune):
    return quarter_turn_right(quarter_turn_right(rune))

##show(turn_upside_down(sail_bb))










#question 4
def quarter_turn_left(pic):
    return quarter_turn_right(quarter_turn_right(quarter_turn_right(pic)))

##show(quarter_turn_left(sail_bb))










#question 6
def try_this(pic1, pic2):
    return beside(pic2, pic1)

##show(try_this(circle_bb, nova_bb))













#question 7
def repeated_stack(pic1, pic2):
    return stack(stack(turn_upside_down(pic1), pic2), pic1)
















#question 8
eyes = beside(make_cross(nova_bb), spiral_bb)

square = beside(beside(blank_bb, beside(blank_bb, black_bb)),
                beside(beside(black_bb, blank_bb), blank_bb))

triangle = beside(quarter_turn_left(flip_horiz(sail_bb)),
                  quarter_turn_right(sail_bb))

show(stack(stack(eyes, square), triangle)) 

