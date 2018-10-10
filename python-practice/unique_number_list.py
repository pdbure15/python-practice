'''
Given a list of numbers with some duplicates,
return non-repeated(unique) number in the list
'''
def uniqueNum(numList):

	finalList = []

	numDict = {}

	for e in numList:
		numDict[e] = numList.count(e)

		if numDict[e] == 1:
			print 'Unique number in the list is ', e
	
	print numDict


if __name__ == '__main__':
	lst = [1,1,2,3,4,3,4]
	uniqueNum(lst)