'''
Selection Sort
'''
A = [64, 25, 12, 22, 11]
 
# Traverse through all array elements
for i in range(len(A)):
	print 'Value of I-',i

	min_idx = i
	for j in range(i+1, len(A)):
		print 'Value of J -',j
		if A[min_idx] > A[j]:
			min_idx = j
			print 'Minimum Index -',min_idx
	         
	# Swap the found minimum element with 
	# the first element        
	A[i], A[min_idx] = A[min_idx], A[i]
 
# Driver code to test above
# print ("Sorted array")
# for i in range(len(A)):
#     print("%d" %A[i]) 