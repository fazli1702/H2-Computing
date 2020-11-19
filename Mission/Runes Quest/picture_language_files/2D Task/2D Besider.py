from runes import*

def besider(n, rune):
    result = rune
    for i in range(n):
        result = stack_frac(1/(i+1), quarter_turn_left(rune), result)
    return (quarter_turn_right(result))



show(besider(7, heart_bb))
