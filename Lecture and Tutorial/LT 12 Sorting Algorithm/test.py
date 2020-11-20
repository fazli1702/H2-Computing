arr = [3, 6, 8, 2, 1, 9]
print('array:')
print(arr)



def bubble_sort(arr):
    swap = True
    end = len(arr)-1
    while swap and end > 0:
        swap = False
        for i in range(end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr

# print('bubble_sort:')
# print(bubble_sort(arr))



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr


# print('insertion_sort:')
# print(insertion_sort(arr))




def selection_sort(arr):
    for i in range(len(arr)-1):
        largest_i = i
        largest = arr[largest_i]
        for j in range(i, len(arr)):
            if arr[j] > largest:
                largest_i = j

        if i != largest_i:
            arr[i], arr[largest_i] = arr[largest_i], arr[i]

    return arr[::-1]

# print('selection_sort:')
# print(selection_sort(arr))



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    lst = []
    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            lst.append(right.pop(0))
        else:
            lst.append(left.pop(0))

    if len(left) != 0:
        lst += left

    elif len(right) != 0:
        lst += right

    return lst

print('merge_sort:')
print(merge_sort(arr))
