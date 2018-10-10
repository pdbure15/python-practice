# -*- coding: utf-8 -*-
"""
Question 1: Write a Python function to check if a number is prime or not.
-------------------------------------------------------------------------

"""


def is_prime(num):
    """
    This function takes a number as argument and checks if it is prime or not.

    Args:
        num (int): an integer number.

    Returns:
        bool: The return value. True if prime number, False otherwise.

    Examples:
        >>> is_prime(3)
        True

        >>> is_prime(4)
        False

    **Write your code below**
   """
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False    
    return True

"""
Question 2: Write a Python function to convert RFC 2822 date format to ISO 8601 format.
---------------------------------------------------------------------------------------

"""
from datetime import datetime, timezone

def convert_rfc2822_to_iso8601(rfcdate):
    """
    This function takes a RFC 2822 formatted date string
    and converts it to a ISO 8601 formmated date string.

    Args:
        rfcdate (str): RFC 2822 formatted date string

    Returns:
        str: The return value. ISO 8601 formatted date string

    Examples:
        >>> convert_rfc2822_to_iso8601('Fri, 21 Nov 1997 09:55:06 -0600')
        '1997-11-21T09:55:06-06:00'

        >>> convert_rfc2822_to_iso8601('Tue, 26 Jun 2018 04:00:00 UTC')
        '2018-06-26T04:00:00Z'  # or '2018-06-26T04:00:00+00:00'

    **Write your code below**
    """
    # dt = datetime.datetime.strptime(dt_str, '%a, %d %b %Y %H:%M:%S %z')
    # dt_utc = rfcdate.split(' ')[5]
    # print(dt_utc)

    if rfcdate.split(' ')[5] == 'UTC':
        dt = datetime.strptime(rfcdate, '%a, %d %b %Y %H:%M:%S %Z')
        dt_iso = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, tzinfo = timezone.utc).isoformat()
    else:
        dt_iso = datetime.strptime(rfcdate, '%a, %d %b %Y %H:%M:%S %z').isoformat()
    
    # print(dt_iso)
    return dt_iso

""" 
Question 3: Write a Python class to implement Linked List.
----------------------------------------------------------

Implement a Linked List class that supports the following operations:
    * Insert: inserts a new data node into the list
    * Size: returns size of list
    * Search: searches list for a node containing the requested data and returns that node if found, otherwise raises an error
    * Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error
    * Generator: returns a generator that returns the next data object in the linked list

"""
from random import randint

class Node:

    # To initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    
    # To initialize the linkedlist header and size of linkedlist
    def __init__(self, head=None):
        """
        **Write your code below**
        """
        self.head = head
        self._size = 0

    def insert(self, data):
        """
        **Write your code below**
        """

        # Initialize the Node with data, next pointer values
        new_node = Node(data)

        # If linked-list is empty, set the head to point at new_node
        if self.head is None:
            self.head = new_node
            self._size += 1
            return
        
        # If linked-list is not empty, traverse to the last_node 
        last_node = self.head
        while True:
            if last_node.next == None:
                break
            last_node = last_node.next


        # Set the last_node's next to new_node data, increment the size counter
        last_node.next = new_node
        self._size += 1


    def size(self):
        """
        **Write your code below**
        """
        # Return the size of the list
        return self._size

    def search(self, data):
        """
        **Write your code below**
        """
        current = self.head

        # Traverse the list starting from head node
        while current != None:

            # If node is found, return the node
            if current.data  == data:
                return data
            current = current.next

        # Return an error message if node is not present in the list
        error = str(data) + ' not present in linkedlist.'
        return error


    def delete(self, data):
        """
        **Write your code below**
        """

        # Store head node in a temp var
        temp = self.head

        # If head node contains the data to be deleted
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                self._size -= 1
                return

        # Traverse the list to search for the node to be deleted,
        # keep track of the previous node
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        # If the node is not present in linkedlist
        if temp == None:
            return

        # Unlink the node from linkedlist
        prev.next = temp.next

        temp = None
        self._size -= 1


    def generator(self):
        """
        **Write your code below**
        """
        current = self.head
        while current != None:
            yield current.data
            current = current.next


""" 
Question 4: Write a Python test program using the classes and function above.
-----------------------------------------------------------------------------

Write a test program that uses all functions and LinkedList class defined in above questions.
For example, insert random numbers and RFC 2822 formatted date strings to the LinkedList,
print the initial size of the list, use the generator to convert date string to ISO format,
delete all prime numbers from the list, and print the final size of the resulted list.

Example:
    In the end, this file should be an executable Python program that can demonstrate
    all your answers to the Python programming questions listed above.::

        $ python interview_questionnaire.py

"""
def main():
    """
    **Write your code below**
    """

    # Initialize linkedlist object
    llist = LinkedList()

    #1. Insert random integers in the linkedlist with insert()
    for i in range(16):
        llist.insert(randint(10,40))

    #2. Insert rfc-formatted date strings to linkedlist
    rfcdates = ['Fri, 21 Nov 1997 09:55:06 -0600', 'Thu, 20 Nov 1997 08:50:0 -0600',
                 'Tue, 26 Jun 2018 04:00:00 UTC', 'Wed, 27 Jun 2018 05:00:00 UTC']

    for dates in rfcdates:
        llist.insert(dates)

    show_elements1 = [node for node in llist.generator()]
    print('\n# Elements in Linked-List.')
    print(*show_elements1, sep="-> ")

    #3. Initial Size of the LinkedList
    print('\n# Initial size of the LinkedList -', llist.size(), '\n')

    #4. Generator to convert rfc2822 dates to iso-formatted, 
    #   delete all the prime numbers in the list

    for gendata in llist.generator():

        if isinstance(gendata, int) and is_prime(gendata):
            print('Deleting Prime number - ', gendata, '\n')
            llist.delete(gendata)

        elif isinstance(gendata, str):
            isodate = convert_rfc2822_to_iso8601(gendata)
            print('Input RFC Date > {}\nOutput ISO Date > {}\n'.format(gendata, isodate))

    # Uncomment below code to check elements of linkedlist after prime numbers are deleted
    # show_elements2 = [node for node in llist.generator()]
    # print('\n# Elements in Linked-List post prime number deletion.\n')
    # print(*show_elements2, sep="->")

    # 5. Final Size of the LinkedList
    print('\n# Final size of the LinkedList - ', llist.size(), '\n')

if __name__ == "__main__":
    main()