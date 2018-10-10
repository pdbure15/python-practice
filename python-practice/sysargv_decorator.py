# Sysargv.py
# The Program displays function under execution alongwith the command-line arguments passed

import sys
from functools import wraps

def display_func(func):
	'''Displays function under execution.'''
	
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(f'\nExecuting {func.__name__}...')
		return func(*args, **kwargs)
	
	return wrapper

@display_func
def read_cmd_args():
	'''Displays command line arguments '''
	
	vals = sys.argv[1:]
	print(f'Documentation - {read_cmd_args.__doc__}')
	print(f'Arguments - {vals}')

if __name__ == '__main__':
	read_cmd_args()