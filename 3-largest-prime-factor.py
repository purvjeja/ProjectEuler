import math as math
EXAMINEE = 600851475143

def main():
	largest = 0
	n = EXAMINEE
	for i in xrange(2,int(math.sqrt(EXAMINEE))):
		if(n % i == 0):
			n = n / i
		if(n == 1 or n == i):
			print i
			break
if __name__ == '__main__':
	main()