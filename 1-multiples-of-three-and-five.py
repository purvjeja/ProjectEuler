def main():
	sum = 0
	for x in xrange(1,1000):
		shouldBeIncluded = (isDivisibleByThree(x) or isDivisibleByFive(x))
		if shouldBeIncluded:
			sum = sum+x
	print sum

def isDivisibleByThree(n):
	if n%3 == 0:
		return True
	else:
		return False

def isDivisibleByFive(n):
	if n%5 == 0:
		return True
	else:
		return False


if __name__ == '__main__':
	main()
