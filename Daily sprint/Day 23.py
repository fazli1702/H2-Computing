def split(string):
    if len(string) == 0:
        return (0, '')
    elif len(string) == 1:
        return (1.0, string)
    else:
        return (float(string[:-1]), string[-1])


print(split('34x'))
print(split('0.5a'))
print(split('x'))
print(split(''))
