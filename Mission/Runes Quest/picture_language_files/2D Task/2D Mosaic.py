from runes import*

def mosaic(pic1, pic2, pic3, pic4):
    return beside(stack_frac(1/2, pic4, pic3), stack_frac(1/2, pic1, pic2))


show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))
    
