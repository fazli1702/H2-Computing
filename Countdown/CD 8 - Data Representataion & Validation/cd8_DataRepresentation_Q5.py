def HexaToDenary(s):
    key = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    den = 0
    s = s[::-1]
    for i in range(len(s)):
        if s[i] != '0':
            if s[i].isdigit():
                den += int(s[i]) * (16**i)
            else:
                den += key[s[i]] * (16**i)
    return den


def display():
    code = '03B'
    print('%-10s %-10s %-10s' % ('Unicode', 'Character', 'Denary Value'))
    char = ['\u03B1', '\u03B2', '\u03B3', '\u03B4', '\u03B5', '\u03B6', '\u03B7', '\u03B8']
    for i in range(1, 9):
        unicode = code + str(i)
        den = HexaToDenary(unicode)
        print('%-10s %-10s %-10s' % (unicode, char[i-1], den))


##display()
        
        
