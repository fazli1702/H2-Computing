def raw_score(x):
    total = 0
    for i in range(len(x)):
        if x[i] == 'X':
            total += 10
        else:
            total += int(x[i])
    return total
    
def count_strike(x):
    strike = 0
    for i in range(len(x)):
        if i == len(x)-1 or i == len(x)-2:
            strike += 0

        elif x[i] == 'X' and x[i+1] == 'X' and x[i+2] == 'X':
            strike += 20

        elif x[i] == 'X' and x[i+1] == 'X':
            strike += 10 + int(x[i+2])

        elif x[i] == 'X':
            strike += int(x[i+1]) + int(x[i+2])
            
        else:
            strike += 0

    return strike

def delete_letter(msg, letter):
    if msg == '':
        return ''
    elif msg[0] == letter:
        return delete_letter(msg[1:], letter) 
    else:
        return msg[0] + delete_letter(msg[1:],letter)

def count_spare(x):
    spare = 0
    spare_score = 0
    y = delete_letter(x, 'X')
    for i in range(len(y)):
            
        if int(y[-3]) + int(y[-2]) == 10 or int(y[-1]) + int(y[-2]) == 10 :
            spare_score += 0
        
        elif i % 2 == 0:
            spare = 0
            spare += int(y[i])
        
        elif i % 2 == 1:
            spare += int(y[i])
            
        elif spare == 10:
            spare_score += int(y[i+1])
            

    return spare_score

def bowling_score(params):
    if params == 'XXXXXXXXXXXX':
        return 300
    else:
        return raw_score(params) + count_strike(params) + count_spare(params)

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





        
        
        
        
