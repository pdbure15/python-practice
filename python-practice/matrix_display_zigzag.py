'''
Print the Matrix in ZigZag form


INPUT	1 2 3 
		4 5 6 
		7 8 9

OUTPUT - 1 2 3 6 5 4 7 8 9

'''

def displayZigZag(matrix):

	for i in range(len(matrix)):

		if i % 2 == 0:
			for j in range(len(matrix[i])):
				print matrix[i][j],
		else:
			for j in range( len(matrix[i])-1 , -1, -1):
				print matrix[i][j],


if __name__ == '__main__':
	matrix = [ [1,2,3], [4,5,6], [7,8,9] ]

	displayZigZag(matrix)