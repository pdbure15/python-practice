'''
Queue implementation
Elements - Front, Rear, maxSize
Operations - Enqueue(Add), Dequeue(Remove)
'''

class Queue(object):

	def __init__(self):
		self.maxSize = 10
		self.arr = [None] * self.maxSize
		self.front = -1
		self.rear = -1

	def __repr__(self):
		return 'Array - {}, \nFront value {}, Rear value {}'.format(self.arr, self.front, self.rear)

	def isEmpty(self):
		
		if self.front == self.rear:
			self.front = self.rear = -1
			return True

		return False

	def isFull(self):
		return self.front == self.maxSize

	def enqueue(self, element):

		if not self.isFull():
			self.front += 1
			self.arr[self.front] = element

		print 'Element {} added to queue.'.format(element)

	def deque(self):

		if self.isEmpty():
			return 'No elements to remove from queue.'
		
		self.rear += 1
		lastElement = self.arr[self.rear]
		self.arr[self.rear] = None

		return lastElement

if __name__ == '__main__':
	queue1 = Queue()

	queue1.enqueue(10)
	queue1.enqueue(20)
	queue1.enqueue(30)

	print queue1.deque()
	print queue1.deque()
	print queue1.deque()
	print queue1.deque()
	# print queue1

	queue1.enqueue(40)
	print queue1

