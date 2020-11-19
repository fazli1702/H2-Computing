from runes import*

def simple_fractal(pic):
    return beside(pic, stack_frac(1/2, pic, pic))

show(simple_fractal(heart_bb))
