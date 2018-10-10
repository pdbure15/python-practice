'''

#1. Calculate score of the words by alphabetic-order i.e. B/b-2, C/c-3
	
	#1.1 For vowels, double their value i.e. A/a-2, O/o-30
	EX:- MOO => M + O + O => 13 + (15*2) + (15*2) = 73

	#1.2 Ignore-case while calculating the scores

#2. Sort the list of words based on the sum of words score

	#2.2 In case two words have same scores, don't change their order in list

	# 'moo' : , 'MOO' : 

'''

from collections import OrderedDict

def score_word(words):
	
	'''
	Need OrderedDict() in order to preserve the order in which 
	values are inserted in the Dictionary
	'''
	wordDict = OrderedDict()

	wordTuple = []


	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

	for word in words:
		if word.isalpha():
			upper = range(65, 91)
			lower = range(97, 123)
			wordValue = 0

			print 'Word - {} in process..'.format(word)

			for char in word:
				if ord(char) in lower:
					if char in vowels:
						valueToAdd = (lower.index(ord(char)) + 1) * 2
						wordValue += valueToAdd
					else:
						valueToAdd = lower.index(ord(char)) + 1
						wordValue += valueToAdd
				
				if ord(char) in upper:
					if char in vowels:
						valueToAdd = (upper.index(ord(char)) + 1) * 2
						wordValue += valueToAdd
					else:
						valueToAdd = upper.index(ord(char)) + 1
						wordValue += valueToAdd

			wordTuple.append((word, wordValue))

	
	print 'Word Tuple list - ', wordTuple
	sorted_tuple = sorted(wordTuple, key=lambda x:x[1] )
	print 'Sorted Tuple - ', sorted_tuple


def checkAlphabets(names):
	for name in names:
		if name.isalpha():
			print 'Processing - {}'.format(name)


if __name__ == '__main__':
	namesList1 = ['Pranay', 'Peter', 'Anjali']
	namesList2 = ['that', 'Moo', 'This', 'MOO']
	namesList3 = ['Pranay', 'Pranay', 'Pranay']
	score_word(namesList3)

	# checkAlphabets(namesList1)