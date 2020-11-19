arr = [5, 4, 3, 2, 1]

def bubbleSort(arr):
	counter = 0
	for i in range(len(arr)):
		for j in range(len(arr)-1):
			counter += 1
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	print(counter)
	return arr

# print(bubbleSort(arr))

def oppBubbleSort(arr):
	counter = 0
	n = len(arr)-1
	while True:
		swap = False
		for i in range(n):
			counter += 1
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				swap = True
		n -= 1

		if swap == False:
			break
	
	print(counter)
	return arr


# print(oppBubbleSort(arr))


def insertionSort(arr):
	

