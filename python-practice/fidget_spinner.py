# Complete the waitingTime function below.
# Given a list *spinners* with values suggesting the amount of spinners to collect
# Matt's position is defined as P
# Calculate the amount of time it takes for Matt to collect spinners based on his position
# spinners[spiner[0].... spinner[n-1]] - Array of spinners desired by each person at position i 
# p: Matt's position in line

import math
import os
import random
import re
import sys

def waitingTime(spinners, p):

	timeToCollect = 0

	'''
	In a given list of spinners, decrease the count of Matt's spinners, 
	until it's equivalent to 1,
	With every pass add the length of list to timeToCollect variable to keep track of unit time
	'''
	while spinners[p] != 1:
		spinners = [ s-1 for s in spinners]
		timeToCollect += len(spinners)

	'''
	Check for the value 0 in the sub-list from Matt's position to the starting index of the list,
	Iff values are GT 0 increase the timeToCollect counter by 1 and return timeToCollect
	'''
	for element in spinners[:p+1]:

		if element > 0:
			timeToCollect += 1

	return timeToCollect


if __name__ == '__main__':
	spinners = [2,6,3,4,5]
	p = 0
	result = waitingTime(spinners, p)

	print '''\nSpinners - {}, Matt wants to collect {} spinners.\nWaiting time to collect {} spinner(s)
	is {} units of time.'''.format(spinners,spinners[p],spinners[p], result)