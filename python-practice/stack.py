'''
Stack implementation
'''

class Stack(object):

	def __init__(self):
		self.top = -1
		self.maxSize = 10
		self.arr = [None] * self.maxSize
		


	def __repr__(self):
		return 'Top is {}, Stack is {}'.format(self.top, self.arr)

	def isFull(self):
		return self.top == 9

	def isEmpty(self):
		return self.top == -1


	'''
	During Push operation check whether stack isn't full,
	then add element at list[top+1], increase value of top by 1
	'''
	def push(self, element):

		if not self.isFull():
			index = self.top + 1
			self.arr[index] = element
			self.top += 1
		print 'Element - {} added to stack'.format(element)


	'''
	During Pop operation check whether stack is empty, if stack is not empty
	then store element to pop and decrease the value of top by 1
	'''

	def pop(self):

		if self.isEmpty():
			print 'No element to pop.'

		lastTop = self.arr[self.top]
		self.arr[self.top] = None
		self.top -= 1
		return lastTop



if __name__ == '__main__':

	stack1 = Stack()
	stack1.push(18)
	stack1.push(12)
	stack1.push(30)
	print stack1.pop()
	print stack1
