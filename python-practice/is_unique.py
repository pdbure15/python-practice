# IS_UNIQUE

def is_unique(data):
	'''Checks for a string uniqueness'''

	# Solution - 1 - Bad solution till now
	# traversedChar = []
	# for char in data:
	# 	traversedChar.append(char)
	# 	if data.count(char) > 1 and char in traversedChar:
	# 		print('String is not unique')
	# 		break
	# else:
	# 	print('Sting is unique.')


	# Solution - 2 - A bit acceptable
	if len(data) == len(set(data)):
		print('String is unique')
	else:
		print('String is not unique')


if __name__ == '__main__':
	# is_unique('Brucee')
	is_unique('Halo')
