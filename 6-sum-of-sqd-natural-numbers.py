def sumOfFirstHundredNNSqd():
    sum = 0
    for i in xrange(1,101):
        sum = sum + i
    return sum**2

def sumOfSqdHundredNN():
    sum = 0
    for i in xrange(0,101):
        sum = sum + (i**2)
    return sum

def main():
    print sumOfFirstHundredNNSqd() - sumOfSqdHundredNN()

if __name__ == '__main__':
	main()