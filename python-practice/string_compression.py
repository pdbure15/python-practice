#string_compression.py

def string_compression(string):
	'''Returns compressed string with the count of characters'''
	count = 0
	compressed = []

	for i in range(len(string)):

		if i != 0 and string[i] != string [i - 1]:
			compressed.append(string[i-1]+str(count))
			count = 0
		count += 1

	# Add last repeated character to compressed list
	compressed.append(string[-1] + str(count))

	return min(string,''.join(compressed), key=len)


if __name__ == '__main__':
	result = string_compression('aaaa')
	print(result)