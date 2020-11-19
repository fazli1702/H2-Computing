def bowling_score(parameter):

    total = 0
    x = 0
    lst = []
    lst.extend(parameter)

    for i in range(len(lst)):
        if lst[i] == 'X':
            lst[i] = 10
        elif type(lst[i]) == str:
            lst[i] = int(lst[i])
        else:
            continue

    while x < len(lst):
        

        if len(lst) == 3 or len(lst) == 2 or len(lst) == 1:
            total += lst[x]
            del lst[x]

        elif lst[x] == 10:
            total += 10 + lst[x+1] + lst[x+2]
            del lst[x]

        elif lst[x] + lst[x+1] == 10:
            total += 10 + lst[x+2]
            del lst[x: x+2]

        else:
            total += lst[x] + lst[x+1]
            del lst[x: x+2]

    return total




print(bowling_score("X7390X088206XXX81")) # == 167
print(bowling_score("00000000000000000000")) # == 0
print(bowling_score("XXXXXXXXXXXX")) # == 300
print(bowling_score("919191919191919191919")) # == 190
print(bowling_score("10101010101010101010")) # == 10
print(bowling_score("X91X91X91X91X91X")) # == 200
print(bowling_score("00X00X00X00X00X00")) # == 50
print(bowling_score("192837465564738291XXX")) # == 174
print(bowling_score("555555555555555555555")) # == 150
print(bowling_score("X714353726180268152")) #  == 89
print(bowling_score("111111111111111111X11")) # == 30
print(bowling_score("111111111111111111X91")) # == 38
print(bowling_score("X911111111111111111")) # == 47
