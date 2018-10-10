# URLIFY string spaces with %20 chars

def urlify(sentence, length):

	new_index = len(sentence)

	# for i in reversed(range(length)):

	# 	if sentence[i] == ' ':
	# 		sentence[new_index - 3:new_index] = '%20'
	# 		new_index -= 3
	# 	else:
	# 		sentence[new_index - 1] = sentence[i]
	# 		new_index -= 1

	# print(sentence)

	result = ["%20" if char == ' ' else char for char in sentence.rstrip()]

	print(''.join(result))



if __name__ == '__main__':
	urlify('Mr Pranay Bure  ', 14)
	# urlify('Mr Pranay Bure', 14)