# TASK 2.1
# Codes for 
# A : CalCheckDigit(Number, Total)
# B : return 'X'
# C : Number + CheckValue

# TASK 2.2
# Program Code:

def CalCheckDigit(Number, Total):
    if len(Number) > 1:
        Digit = int(Number[0])
        Total += (Digit * (len(Number)+1))
        NewNumber = Number[1:]
        CheckDigit = CalCheckDigit(NewNumber, Total)
    else:
        Digit = int(Number[0])
        Total += (Digit * (len(Number)+1))
        CalcModulus = Total % 11
        CheckValue = 11 - CalcModulus

        if CheckValue == 11:
            return str(0)
        elif CheckValue == 10:
            return 'X'
        else:
            return str(CheckValue)

    if len(Number) == 9:
        return Number + CheckDigit
    else:
        return CheckDigit



##print(CalCheckDigit("075154926", 0))
##print(CalCheckDigit("034085045", 0))
##print(CalCheckDigit("184146208", 0))
