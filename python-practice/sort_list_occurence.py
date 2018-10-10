# Sort the list based on the number of occurences of elements

from collections import Counter

num = [3,4,1,6,6,2,5,2,7,-1, -1, -2]

num2 = dict(Counter(sorted(num)))
num3 = dict(sorted(num2.items(), key = lambda x:x[1]))
num4 = []
# print('\nNUM2 - {}\nNUM3 - {}'.format(num2, num3))

for k,v in num3.items():
	num4.extend(v*[k])

print(*num4, sep='\n')