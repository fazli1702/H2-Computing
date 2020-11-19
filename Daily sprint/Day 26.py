lst = [['USD',0.7443],['EUR',0.6274],['GBP',0.5570],['KRW',801.4624],['IDR',10098.18],['MYR',3.0361],['JPY',84.3113],['HKD',5.8182]]

def currex(lst,currency,amount):
    for ele in lst:
         if currency in ele:
            sgd = int(amount / ele[1])
            return str(sgd) + 'SGD'
    return 'Currency not found.'
        

    

print(currex(lst,'USD',15.90))
print(currex(lst,'KRW',20900))
print(currex(lst,'BTC',12))
