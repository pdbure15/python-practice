#palindrome_permutation.py

#What are qualities of a palindrome string? 
#It has EVEN number counts of characters or at most just ONE character with an ODD count.
 #>>>This means the string is either of even length or an odd length with just exactly one character with an odd count.<<<

 #What you need is to find out if there is at most one "single" letter (and others are paired). 
 #Thus we count the letters with collections.Counter and ensure that only 0 or 1 of them has odd count:

from collections import Counter

def check_palindrome_permutation(string):
	'''Checks if the string is a palindrome permutation or not '''
	cntr = Counter(string.lower())

	countodd = 0
	for char in cntr:
		if char != ' ' and cntr[char] == 1:
			# print('Char - ', char)
			countodd += 1

	# printc(ountodd)

	return countodd <= 1



if __name__ == '__main__':
	result1 = check_palindrome_permutation('Random Words')
	result2 = check_palindrome_permutation('Taco Cat')
	print(result1)
	print(result2)