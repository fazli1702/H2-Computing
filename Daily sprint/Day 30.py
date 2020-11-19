def convert(km, unit, lst):
    if unit == 'mile' or unit == 'mi':
        return round(km * lst[0], 5)
    elif unit == 'feet' or unit == 'ft':
        return round(km * lst[1], 5)
    elif unit == 'inches' or unit == 'in':
        return round(km * lst[2], 5)
    elif unit == 'centimetres' or unit == 'cm':
        return round(km * lst[3], 5)
    else:
        return 'Unknown unit'

lst = [0.62137119223733, 3280.8398950131, 39370.078740157, 100000]


print(convert(24, 'Mile', lst))
print(convert(24, 'mile', lst))
print(convert(24, 'mi', lst))
print(convert(18.3, 'feet', lst))
print(convert(18.3, 'ft', lst))
