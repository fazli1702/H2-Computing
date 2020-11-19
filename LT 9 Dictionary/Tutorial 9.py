#question 1
def count_letters(word):
    new_word = []
    new_dict = {}
    for i in range(len(word)):
        new_word += word[i]

    for ele in new_word:
        if ele not in new_dict:
            new_dict[ele] = (new_word.count(ele))
        else:
            continue
    return new_dict

##print(count_letters('apples'))
        










#question 2
def count_vowels(word):
    new_word = []
    new_dict = {}
    for i in range(len(word)):
        new_word += word[i]

    for ele in new_word:
        if ele == 'a' or ele == 'e' or ele == 'i' or ele == 'o' or ele == 'u':
            if ele not in new_dict:
                new_dict[ele] = (new_word.count(ele))
            else:
                continue
    return new_dict
            


##print(count_vowels('apple'))
    















#question 3
def dict_print(d):
    for k,v in d.items():
        print(k)
        print(v)


test_data = { "couple":2, "dozen": 12, "gross":144, "score":20 }
##print(dict_print(test_data))





#question 4
burger = {'ham':47, 'chicken': 75, 'fish': 27}  


def total(items):
    total = 0
    for value in burger.values():
        total += value
    return total

def add(item, qty):
    burger[item] += qty
    return burger

##print(total(burger))
##print(add('fish', 5))













#question 5
def average(result1, result2):
    new_dict = {}
    for key in result1:
        new_dict[key] = (result1[key] + result2[key]) / 2
    return new_dict


CT1 = {'H1GP': 58, 'H2MA': 66, 'H2CP': 75, 'H2PH': 55, 'H1EC': 45}
CT2 = {'H1GP': 62, 'H2MA': 73, 'H2CP': 72, 'H2PH': 61, 'H1EC': 47}   
    
##print(average(CT1, CT2))











#question 6
def top3(products):
    x = len(products) - 3
    new_dict = {}
    max_value = 0
    max_key = ''
    while len(products) > x:
        for key in products:
            if products[key] > max_value:
                max_value = products[key]
                max_key = key
            else:
                continue
        new_dict[max_key] = max_value
        del products[max_key]
        max_value = 0
        max_key = ''
    return new_dict



models = {'Samsung Galaxy S10': 230, 'Huawei P30': 352, 'iPhone XS': 287, 'Samsung Note 9': 186, 'Google Pixel 3XL': 120, 'LG G7 ThinQ': 93}
food = {'chicken wing': 87, 'apple pie': 186, 'donut': 52, 'coffee': 120, 'ice cream': 30, 'cake': 93}

##print(top3(models))
##print(top3(food))
