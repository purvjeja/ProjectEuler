def main():
	n1 = 100
	n2 = 100
	maxProd = 0
	for i in xrange(n1,1000):
		for j in xrange(i,1000):
			if(isPalindromic(i * j)):
				if(i * j > maxProd):
					maxProd = i * j
	print maxProd

def isPalindromic(n):
	numAsStr = str(n)
	i = 0
	j = len(numAsStr) - 1
	while(1):
		if(numAsStr[i] == numAsStr[j]):
			j = j - 1
			i = i + 1
		else:
			return False

		if(i >= j):
			return True

if __name__ == '__main__':
	main()