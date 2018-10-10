'''
Count number of duplicates in Python list
'''

def countDupes(lst):

	tempList = list(set(lst))
	duplicateDict = {}

	for char in tempList:
		duplicateDict[char] = lst.count(char)
		print '{} - {}'.format(char, lst.count(char))

	print 'Dictionary\n',duplicateDict



if __name__ == '__main__':
	lst = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']
	countDupes(lst)