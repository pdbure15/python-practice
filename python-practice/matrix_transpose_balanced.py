'''
Print Tranpose of Matrix

***INPUT***
	1 2 3
	4 5 6
	7 8 9

***OUTPUT***
	1 4 7
	2 5 8
	3 6 9

'''

def transposeMatrix(matrix):

	for i in range(len(matrix)):

		for j in range(len(matrix[i])):
			print matrix[j][i],
		print '\n'


if __name__ == '__main__':

	matrix = [ [1,2,3], [4,5,6], [7,8,9]]

	transposeMatrix(matrix)