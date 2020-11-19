# task 1.1
with open('WORDS1.txt', 'r') as f:
    data = f.readlines()
    words = []
    occurence = []
    i = 0
    for row in data:
        row = row.strip()
        if i == 0:
            words.append(row)
            i += 1
        else:
            occurence.append(int(row))
            i = 0


for i, ele in enumerate(occurence):
    if ele == max(occurence):
        break
        print(words[i])


# task 1.2
with open('WORDS2.txt', 'r') as f:
    data = f.readlines()
    words = []
    occurence = []
    i = 0
    for row in data:
        row = row.strip()
        if i == 0:
            words.append(row)
            i += 1
        else:
            occurence.append(int(row))
            i = 0


for i, ele in enumerate(occurence):
    if ele == max(occurence):
        break
        print(words[i])
        





        

