'task 1.1'

with open('INVENTORY.txt') as f:
    data = f.readlines()
    Inventory = [row.strip() for row in data]

##print(Inventory)

ItemTypes = []
for ele in Inventory:
    if ele not in ItemTypes:
        ItemTypes.append(ele)

##print(ItemTypes)


ItemCounts = []
for item in ItemTypes:
    counter = 0
    for ele in Inventory:
        if item == ele:
            counter += 1
    ItemCounts.append(counter)

##print(ItemCounts)

print('%-17s %-10s' % ('ItemType', 'Count'))
print()
for item, count in zip(ItemTypes, ItemCounts):
    print('%-17s %-10s' % (item, count))
