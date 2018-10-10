'''
Bubble Sort: Iterative & recursive
'''

def BubbleSort(arr):

	n = len(arr)

	for i in range(n):

		print 'PASS-{} in execution.'.format(i)

		for j in range(0, n-i-1):

			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

def rec_bubble_sort(listt):
    for i, num in enumerate(listt):
    	print 'Index is ',i
        try:
            if listt[i+1] < num:
                listt[i] = listt[i+1]
                listt[i+1] = num
                print 'Array in {} pass is {}'.format(i, listt)
                rec_bubble_sort(listt)
        except IndexError:
            pass
    return listt

if __name__ == '__main__':

	numbers = [64, 34, 25, 12, 22, 11, 90]
	numbers2 = [64, 34, 25, 12, 22, 11, 90]

	# BubbleSort(numbers)

	result = rec_bubble_sort(numbers2)
	print result

	# print 'Sorted numbers\n',numbers 
	# for n in numbers:
	# 	print n

