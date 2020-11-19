import csv

def read_file():
    with open('ADMISSIONS-DATA.txt') as f:
        info = csv.reader(f)
        data = [ele[0] for ele in info]
    return data

def bubble_sort(arr):
    NoSwaps = False
    counter = 0
    while not NoSwaps:
        NoSwaps = True
        for i in range(len(arr)-1):
            counter += 1
            if arr[i] > arr[i+1]:
                NoSwaps = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr, counter
                

def insertion_sort(arr):
    counter = 0
    for i in range(1, len(arr)-1):
        j = i-1
        key = arr[i]
        counter += 1
        while j >= 0 and key < arr[j]:
            counter += 1
            arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, counter



# task 1.1
def main():
    while True:
        print('1. Read file data')
        print('2. Bubble sort')
        print('3. Quick sort / Insertion sort')
        print('4. End')

        choice = input('Please enter your choice:')
        
        # task 1.2
        if choice == '1':
            data = read_file()
            print(data)

        if choice == '2':
            print(bubble_sort(data))

        if choice == '3':
##            print(insertion_sort(data))
            print(quick_sort(data))
        
        if choice == '4':
            break

main()
