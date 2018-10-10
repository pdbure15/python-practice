# test_random_generator.py
# Testing random_generator.py functions
import pytest
from random_generator import generate_random_nums

def test_multiple_values_generate_random_nums():
	'''Verifies the ValueError exception in case requested sample is greater than length of the number list'''
	
	#Approach-1
	expected = 'Sample larger than population or is negative'
	num_lst = [1,2,3,4,5]
	sample = 8
	with pytest.raises(ValueError, message = expected):
		res = generate_random_nums(num_lst, sample)

	#Approach-2
	# num_lst = [1,2,3,4,5]
	# sample = 3
	# with pytest.raises(ValueError) as excinfo:
	# 	res = generate_random_nums(num_lst, sample)
	# 	assert 'Sample larger than population or is negative' in str(excinfo.value)

	#Approach-3
	# num_lst = [1,2,3,4,5]
	# sample = 8
	# res = generate_random_nums(num_lst, sample)
	# assert res == None

def test_single_generate_random_nums():
	'''Verifies whether generated random number is present in given list'''

	num_lst = [1,2,3,4,5]
	sample = 1
	num = generate_random_nums(num_lst, sample)
	assert num[0] in num_lst
	# assert generate_random_nums([1,2,3,4], 1)[0] in [1,2,3,4]

# @pytest.mark.xfail(raises=ValueError)
# def test_multiple_values_generate_random_nums():
# 	'''Raises ValueError in case requested sample is greater than length of the number list'''

# 	num_lst = [1,2,3,4,5]
# 	sample = 8
# 	res = generate_random_nums(num_lst, sample)
# 	assert res,ValueError('Sample value larger than input-size.')