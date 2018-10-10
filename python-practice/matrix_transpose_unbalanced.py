'''
Print Tranpose of Matrix if elements are not in order

**INPUT**
1 2 3 10 
4 5 6
7 8 9

**OUTPUT**
1 4 7
2 5 8
3 6 9
10

'''

def adjustMatrixSize(matrix):

	tempMatrix = [len(element) for element in matrix]

	maxlength = max(tempMatrix)

	'''
	Add equivalent columns/ rows to adjust matrix size
	'''

	for i in range(maxlength - len(matrix)):
		matrix.append(['']*maxlength)


	'''
	Add extra spaces/ None in matrix array where elements are less
	'''
	for element in range(len(matrix)):
		if len(matrix[element]) != maxlength:			
			matrix[element].append('')
			# print matrix[element]

	return matrix

def checkMatrixSize(matrix):
	'''
	Check whether Matrix is in proper X*X order, if not then adjust it
	'''
	for element in matrix:
		if len(element) != len(matrix):
			matrix = adjustMatrixSize(matrix)

	transposeMatrix(matrix)



def transposeMatrix(matrix):
	'''
	Transpose a Matrix of X*X size
	'''

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print matrix[j][i],
		print '\n'


if __name__ == '__main__':

	matrix = [ [1,2,3,10], [4,5,6,11], [7,8,9] ]

	checkMatrixSize(matrix)