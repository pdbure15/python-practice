'''
Overiding
'''

class Parent(object):

	def display(self):
		print 'Parent'

	def display(self, name, last):
		print 'Parent Class attributes - {} {}'.format(name, last)

class child(Parent):

	def display(self):
		print 'Child'

p = Parent()
c = child()

p.display('Pranay', 'Bure')
c.display()