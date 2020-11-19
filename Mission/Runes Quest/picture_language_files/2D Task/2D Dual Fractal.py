from runes import*

def dual_fractal(pic1, pic2, n):
    if n == 1:
        return pic1
    else:
        return beside(pic1, stacker(2, dual_fractal(pic2, pic1, n-1)))

show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
