# random_generator.py
# Generates a set of random values from a list of numbers
import random

def generate_random_nums(num_lst, val = 1):
	'''Generate a list of random values from given numbers '''
	
	try:
		result = random.sample(num_lst, val)
	except ValueError as e:
		print(e,'\n')
		# raise # Uncomment this line in case you want to test the code including try-except block
	else:
		return result


	# result = random.sample(num_lst, val)
	# return result


if __name__ == '__main__':
	result = generate_random_nums((1,2,3,4,5), 8)
	print('RESULT - ', result)
