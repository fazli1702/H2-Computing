from runes import*

def steps(pic1, pic2, pic3, pic4):
    layer_1 = stack(beside(pic4, blank_bb), beside(blank_bb, blank_bb))
    layer_2 = stack(beside(blank_bb, blank_bb), beside(pic3, blank_bb))
    layer_3 = stack(beside(blank_bb, pic1), beside(blank_bb, blank_bb))
    layer_4 = stack(beside(blank_bb, blank_bb), beside(blank_bb, pic2))
    return overlay(overlay(layer_1, layer_2), overlay(layer_4, layer_3))

show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
