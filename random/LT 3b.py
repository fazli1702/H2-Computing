def tax_cal(income):
    
    if income <= 20000:
        return 0
    
    elif 20000 < income <= 30000:
        return int(0.02 * (income - 20000))
    
    elif 30000 < income <= 40000:
        return int(200 + 0.035 * (income - 30000))
    
    elif 40000 < income <= 80000:
        return int(550 + 0.07 * (income - 40000))
    
    elif 80000 < income <= 120000:
        return int(3350 + 0.115 * (income - 80000))
    
    elif 120000 < income <= 160000:
        return int(7950 + 0.15 * (income - 120000))
    
    elif 160000 < income <= 200000:
        return int(13950 + 0.18 * (income - 160000))
    
    elif 200000 < income <= 240000:
        return int(21150 + 0.19 * (income - 200000))
    
    elif 240000 < income <= 280000:
        return int(28750 + 0.195 * (income - 240000))
    
    elif 280000 < income <= 320000:
        return int(36550 + 0.20 * (income - 280000))
    
    else:
        return int(44500 + 0.22 * (income - 320000))



print(tax_call(15000))
print(tax_call(25000))
print(tax_call(35000))
print(tax_call(60000))
print(tax_call(100000))
print(tax_call(140000))
print(tax_call(180000))
print(tax_call(220000))
print(tax_call(260000))
print(tax_call(300000))
print(tax_call(330000))
