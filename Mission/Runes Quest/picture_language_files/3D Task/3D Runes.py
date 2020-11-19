from runes import*

def overlay_two(rune):
    return overlay(rune, rune)

def overlay_four(pic):
    return overlay_frac(1/2, overlay(pic, pic), overlay(pic, pic))

show(overlay_four(nova_bb))
