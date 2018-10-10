'''
mergeString(str1, str2) - Return a merged string with alternate characters from two given input strings
 str1 = 'abc'
 str2 = 'defgh'
 
 mergedString = 'adbecfgh'
'''

def mergeString(str1, str2):

	mergedString = ''
	strLenMin = min(len(str1), len(str2))

	for idx in range(strLenMin):
		mergedString += str1[idx] + str2[idx]


	restStr = max(str1, str2, key=len)

	mergedString += restStr[strLenMin:]

	print mergedString

if __name__ == '__main__':
	a,b = 'abcde', 'fgh'
	mergeString(a,b)