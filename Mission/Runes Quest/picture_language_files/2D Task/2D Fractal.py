from runes import*

def fractal(pic,n):
    x = quarter_turn_right(pic)
    for i in range(n-1):
        x = stack_frac(1/(2), quarter_turn_right(pic), beside(x,x))
    return quarter_turn_left(x)

show(fractal(heart_bb, 5))
