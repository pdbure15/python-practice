'''
Implementing Binary Search both Iteratively & recursively
'''

def binary_search(arr, ele):

	first = 0
	last = len(arr) - 1
	found = False

	if len(arr) == 0:
		return found

	while first < last and not found:
		mid = (first + last) / 2

		if arr[mid] == ele:
			found = True
		else:
			if ele < arr[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found


def rec_binary_search(arr, ele):
	first = 0
	last = len(arr) - 1

	if len(arr) == 0:
		return False

	else:
		mid = len(arr) / 2

		if ele == arr[mid]:
			return True
		else:
			if ele < arr[mid]:
				return rec_binary_search(arr[:mid], ele)
			else:
				return rec_binary_search(arr[mid+1:], ele)


if __name__ == '__main__':

	numbers = [44,48,49,53,56,58,60,62,67]

	result1 = binary_search(numbers, 49)

	# print 'Iterative Binary Search result', result1

	result2 = rec_binary_search(numbers, 60)
	print 'Recursive Binary Search result', result2