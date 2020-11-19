from runes import*

def zeno(pic, n):
    if n == 1:
        return pic
    elif n == 2:
        return beside(pic, pic)
    else:
        return beside(pic, zeno(pic, n-1))

show(zeno(make_cross(corner_bb), 9))
