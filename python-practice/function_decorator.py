# Program that displays function-name and its documentation if present, during execution.
from functools import wraps

def displays_func(func):
	'''
	Displays function-name before execution
	'''
	@wraps(func)
	def wrapper(*args, **kwargs):
		'''Prints the function-name where @notify_func decorator is used'''
		print('EXECUTING {}...'.format(func.__name__))
		return func(*args, **kwargs)
	
	return wrapper

@displays_func
def square_nums(number):
	'''Displays square of the number'''
	print('DOCUMENTATION -> {}'.format(square_nums.__doc__))
	return number*number

if __name__ == '__main__':

	number = 5

	square_of_five = square_nums(number)

	print('\nSquare of {} is {}'.format(number, square_of_five))