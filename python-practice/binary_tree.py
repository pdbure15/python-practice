'''
Tree implementation
'''
class BinaryTree(object):

	def __init__(self, root):
		self.key = root
		self.leftchild = None
		self.rightchild = None

	def __repr__(self):
		return 'Root - {}, Left - {}, Right - {}'.format(self.key, self.leftchild, self.rightchild)

	def insertLeft(self, newNode):

		if self.leftchild == None:
			self.leftchild = BinaryTree(newNode)

		else:
			print 'New node is ', newNode
			t = BinaryTree(newNode)
			t.leftchild = self.leftchild
			print '\nT.LEFTCHILD - ', t.leftchild

			self.leftchild = t

			print '\nSELF.LEFTCHILD - ', self.leftchild

	def insertRight(self, newNode):

		if self.rightchild == None:
			self.rightchild = BinaryTree(newNode)

		else:
			t = BinaryTree(newNode)
			t.rightchild = self.rightchild
			self.rightchild = t


if __name__ == '__main__':

	bt = BinaryTree('a')

	bt.insertLeft('b')
	bt.insertLeft('c')