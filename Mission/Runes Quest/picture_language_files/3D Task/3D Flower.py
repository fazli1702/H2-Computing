from runes import*

def flower(pic, num_arms, num_rings):
    return tree(num_rings, (ring(num_arms, pic)))

show(flower(spiral_bb, 5, 5))
    
