MAX_LIMIT = 4000000

def main():
	n1 = 1
	n2 = 2
	n3 = 3
	sum = 2

	while n3 <= MAX_LIMIT:
		n1,n2,n3 = n2,n3,n3+n2
		if(n3%2 == 0):
			sum = sum + n3

	print sum

if __name__ == '__main__':
	main()