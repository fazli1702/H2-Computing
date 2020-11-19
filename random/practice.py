def maxim(lst):
	return max(lst)

#lst = [1, 2, 3]
#print(maxim(lst))


def Sum(arr):
	total = 0
	return sum(arr)
	
#arr = [8, 2, 3, 0, 7]
#print(Sum(arr))



def product(arr):
	total = 1
	for ele in arr:
		total *= ele
	return total 
	
# arr = [8, 2, 3, -1, 7]
# print(product(arr))


def rev(string):
	return string[::-1]
	
string = '1234abcd'
print(rev(string))