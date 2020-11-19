from runes import*

def halo(pic):
    return overlay(scale(1/2, pic), pic)


show(halo(heart_bb))


