from runes import*
def ratio_beside(pic1, pic2, pic3, a, b, c):
    result = stack_frac(a/(a+b+c), quarter_turn_right(pic1), stack_frac(b/(b+c), quarter_turn_right(pic2), quarter_turn_right(pic3)))
    return quarter_turn_left(result)

show(ratio_beside(rcross_bb, pentagram_bb, ribbon_bb, 3,1,2))

