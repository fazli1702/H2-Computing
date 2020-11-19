### Task 2.2 : Exchange rate


exchange={'leather':50,'ore':10,'wood':5, 'scroll':20}
my_bag = {'coin':50,'leather':23,'wood':15,'scroll':2,'ore':13} 

def change_coin(inventory):
    for key, value in inventory.items():
        if key in exchange:
            inventory['coin'] += value * exchange[key]

    lst = []
    for key, value in inventory.items():
        if key != 'coin':
            lst += [key]
            
    for ele in lst:
        del inventory[ele]
        
    return inventory


print(change_coin(my_bag))
