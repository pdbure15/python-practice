import sys

def findDupes(lst1, lst2):
	'''
	Ques1 - Find common elements between two lists
	'''

	result = []

	for num in lst1:
		if num in lst2 and num not in result:
			result.append(num)
	
	return result

def findEldest(data):
	'''
	Ques2 - Read command line arguments and return the name of eldest person

	Check for empty data condition as well..

	Input order will be same
	I/P ->python prog-name.py Peter Bruce Harry 24 26 12
	O/P -> Bruce
	'''

	ages  = []
	names = []

	for element in data:
		if element.isalpha():
			names.append(element)
		else:
			ages.append(int(element))

	print 'NAMES - {}, AGES - {}'.format(names, ages)

	# print 'Maximum age - {}'.format(maxAge)
	
	indexOfAge = ages.index(max(ages))

	print 'ELDEST is {}'.format(names[indexOfAge])


if __name__ == '__main__':
	
	# result = findDupes([1,2,2,3,4,4,1], [1,4,5,2])
	# print 'Common elements from two lists:\n',result

	data = sys.argv[1:]

	findEldest(data)

