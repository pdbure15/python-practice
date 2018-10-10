"""
LinkedList implementation with Node & LinkedList class
Classes - Node, LinkedList
Operations - Add node to linkedlist, Add node between two nodes, Delete node
"""

"""
Create an object of Node class & then pass this nodeObject in LinkedList class - insert/ add/ append method
"""

class Node(object):

	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return '{}'.format(self.data)

class LinkedList(object):

	def __init__(self):
		self.head = None

	def listLength(self):
		current = self.head
		counter = 0
		while current:
			current = current.next
			counter += 1
		return counter

	def showElements(self):
		current = self.head
		while True:
			if current is None:
				break
			print current.data,'->'
			current = current.next

	def add(self, newNode):
		
		if self.head == None:
			self.head = newNode

		else:
			lastNode = self.head

			while True:
				if lastNode.next is None:
					break
				lastNode = lastNode.next

			lastNode.next = newNode

	def addToBeginning(self, newNode):
		while True:
			if self.head is None:
				break
				self.add(newNode)

		self.head, newNode.next = newNode, self.head

	def addBetween(self, newNode, position):
		nodeposition = 0
		position -= 1
		current = self.head

		if position < self.listLength() and position > 0:
			while current is not None:
				nodeposition += 1
				previous = current
				current = current.next

				if nodeposition == position:					
					break
			previous.next = newNode	
			newNode.next = current

	def deleteAt(self, position):
		nodeposition = 0
		position -= 1
		current = self.head

		if position < self.listLength() and position > 0:
			while current is not None:
				nodeposition += 1
				previous = current
				current = current.next

				if nodeposition == position:					
					break
			previous.next = current.next
			del current

	# def reverseList(self):
		


if __name__ == "__main__":
	
	linkedlist = LinkedList()
	node1 = Node('London')
	# linkedlist.addToBeginning(node1)
	linkedlist.add(node1)
	# linkedlist.addToEnd(node1)

	node2 = Node('Mumbai')
	linkedlist.add(node2)

	# # print '\nELEMENTS OF LINKED LIST\n', linkedlist.showElements()

	node3 = Node('Vancouver')	
	linkedlist.add(node3)

	# print '\nELEMENTS OF LINKED LIST\n', linkedlist.showElements()
	node4 = Node('Hawaii')	
	linkedlist.add(node4)

	# linkedlist.showElements()
	# print 'LIST LENGTH - ',linkedlist.listLength()

	node5 = Node('Texas')
	linkedlist.addBetween(node5, 2)
	print 'ORIGINAL LIST'
	linkedlist.showElements()



	linkedlist.deleteAt(2)
	print '\n\nMODIFIED LIST'
	linkedlist.showElements()

