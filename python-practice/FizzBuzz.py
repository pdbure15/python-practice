
'''
Program to display words based on the divisibility test with numbers 3, 5 for the range 1 to 100
'''
def displayCracklePop():

	for num in range(1, 101):

		if num%15 == 0:
			print 'CracklePop ', num
		elif num%3 == 0:
			print 'Crackle ', num
		elif num%5 == 0:
			print 'Pop ', num


if __name__ == '__main__':
	displayCracklePop()