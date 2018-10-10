'''
Rotate Matrix by 90 degree clockwise
'''

def rotateMatrix(Matrix):
	for i in range(len(Matrix)):
		for j in range(len(Matrix)-1, -1, -1):
			print Matrix[j][i],
		print '\n'


if __name__ == '__main__':

	Matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	]
	rotateMatrix(Matrix)